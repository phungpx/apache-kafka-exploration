import uuid
from typing import List
from fastapi import FastAPI, status
from confluent_kafka import Producer
from starlette.responses import JSONResponse
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.serialization import StringSerializer

from logger import Logger
from config import Config
from dto import MessageDto


# FastAPI Application
app = FastAPI()


# ID Generation
def fake_id() -> str:
    return str(uuid.uuid4())


def acked(err, msg):
    '''Delivery report handler called on successful or failed delivery of message.
    '''
    if err is not None:
        logger.logError(f'Failed to deliver message: {err}')
    else:
        logger.logInfo(f'Message Information: topic {msg.topic()} - partition [{msg.partition()}] @ offset {msg.offset()}')


@app.on_event("startup")
async def startup_event():
    global logger
    global producer, admin_client

    # Logger Initialization
    logger = Logger(log_dir=Config.LOG_FOLDER, log_name=Config.LOG_NAME, logging_level='INFO')
    logger.logInfo(f'Setting: {Config.__dict__}')

    # Admin Client and Producer Initialization
    admin_client = AdminClient({'bootstrap.servers': Config.KAFKA_SERVERS})
    producer = Producer({
        'bootstrap.servers': Config.KAFKA_SERVERS,
        # 'batch.size': int(Config.KAFKA_BATCH_SIZE),
        # 'linger.ms': int(Config.KAFKA_LINGER_MS),
    })

    # Topic Creation
    available_topics = admin_client.list_topics().topics
    setting_topics: List[str] = Config.KAFKA_TOPIC.split(',')
    setting_partitions: List[int] = [int(partitions) for partitions in Config.KAFKA_TOPIC_PARTITIONS.split(',')]
    setting_replication_factors: List[int] = [int(factor) for factor in Config.KAFKA_REPLICATION_FACTORS.split(',')]

    new_topics = []

    for (topic, partition, replication_factor) in zip(setting_topics, setting_partitions, setting_replication_factors):
        if topic in available_topics:
            topic_info = available_topics[topic]
            partition_count = len(topic_info.partitions)
            replication_factor_count = len(topic_info.partitions[0].replicas)
            print(f'Topic: {topic} already created.')
            print(f'\tCurrent Partitions: {partition_count}')
            print(f'\tCurrent Replication Factor: {replication_factor_count}')
            for idx, info in topic_info.partitions.items():
                print(f"\tPartition: {idx}, Replicas: {len(info.replicas)}, Belong to: {', '.join(['broker' + str(broker_id) for broker_id in info.replicas])}")

            # if (partition_count != partition) or (replication_factor_count != replication_factor):
            #     # Returns a dict of <topic,future>.
            #     fs = admin_client.delete_topics([topic], operation_timeout=1)

            #     # Wait for operation to finish.
            #     for topic, f in fs.items():
            #         try:
            #             f.result()  # The result itself is None
            #             logger.logInfo("Topic {} deleted".format(topic))
            #             new_topics.append(NewTopic(topic=topic, num_partitions=partition, replication_factor=replication_factor))
            #         except Exception as e:
            #             logger.logError("Failed to delete topic {}: {}".format(topic, e))
        else:
            new_topics.append(NewTopic(topic=topic, num_partitions=partition, replication_factor=replication_factor))

    if len(new_topics):
        created_topic_infos = admin_client.create_topics(new_topics)
        for topic, info in created_topic_infos.items():
            try:
                info.result()  # The result itself is None
                logger.logInfo(f"Topic {topic} created.")
            except Exception as e:
                logger.logError(f"Failed to create topic {topic}: {e}.")


@app.on_event("shutdown")
def shutdown_event():
    logger.logInfo(f"Waiting for all messages in the Producer queue to be delivered.")
    producer.flush()


@app.post("/send-message")
async def send_message(message: MessageDto):
    try:
        if message.topic not in admin_client.list_topics().topics:
            return JSONResponse({
                "statusMessage" : "Topic not found!",
                "statusCode" : status.HTTP_404_NOT_FOUND,
                "errorMessage": f"Topic {message.topic} not found.",
            })

        message_key = fake_id() if Config.MESSAGE_KEYS_RANDOM else message.key
        record_key: bytes = StringSerializer()(message_key)  # <=> encode('utf-8')
        record_value: bytes = StringSerializer()(message.value)  # <=> encode('utf-8')
        producer.produce(
            topic=message.topic,
            key=record_key,
            value=record_value,
            partition=message.partition,
            on_delivery=acked,
        )
        producer.poll(0)
        logger.logInfo(f'Produced message: key={record_key}, value={record_value}.')
        return JSONResponse({
            "statusMessage" : "Message Delivery Complete",
            "statusCode" : status.HTTP_200_OK,
            "message" : message.__dict__,
        })
    except Exception as error:
        logger.logError(f'Producing record failed! with error: {error}')
        return JSONResponse({
            "statusMessage" : "Producing record failed!",
            "statusCode" : status.HTTP_500_INTERNAL_SERVER_ERROR,
            "errorMessage": error,
        })
