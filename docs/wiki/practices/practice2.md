# Practice 2

- Having one consumer group containing 4 consumers and one broker with 3 partitions.

| ![alt text](../../figures/consumer_group/consumers-greater-than-partitions.png?raw=true) |
| :--------------------------------------------------------------------------------------: |
|          _Figure 1: An example of an inactivate consumer in a consumer group._           |

- If I produce a message with `key=None` (do not indicate a specific partition), one of consumers in this consumer group will be inactive. Therefore, we must be set the number of partitions greater than or equal the number of consumers in a consumer group.

- If I produce a message with a specific key to determine what partition receiving messages from producer, just only one consumer will be consume all these messages in that parititon. This leads to some drawbacks for your application in terms of throughput, latency, and cost.

## Docker compose setup

- Run multiple docker compose files (https://stackoverflow.com/questions/62871280/should-i-have-multiple-docker-compose-files)

- Activate all crucial services

```
cd src/docker-compose
docker compose -f dev.docker-compose.yml up
```

- Run producer and consumers

```
cd src/docker-compose
docker compose -f practice2.docker-compose.yml up
```

- Produce message through endpoint `/send-message`

```
URL: http://localhost:8081/send-message
Method: POST
Body:
    {
        "value": "testing-value" (message being produced to consumers)
        // "partition": None (specify partition receiving produced messages)
    }
```

## Terminal Setup

- Acitvate all crucial services including kafka, kafka-ui, zookeeper

```
docker compose -f dev.docker-compose.yml up
```

- Producer with creating a topic name `my-topic` and `3` partitions

```
cd src/producer

# Activate virual environment
python -m venv .venv
source .venv/bin/activate

# Install all dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

```
chmod +x run.sh
KAFKA_TOPIC=my-topic KAFKA_TOPIC_PARTITIONS=3 KAFKA_REPLICATION_FACTOR=1 ./run.sh
```

- Run 4 different consumers in 4 different command panels.

```
cd src/consumer

# Activate virual environment
python -m venv .venv
source .venv/bin/activate

# Install all dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

```
# terminal panel 1 (consumer1-1)
KAFKA_TOPIC=my-topic KAFKA_CONSUMER_GROUP_ID=my-topic-group-1 python consumer

# terminal panel 2 (consumer1-2)
KAFKA_TOPIC=my-topic KAFKA_CONSUMER_GROUP_ID=my-topic-group-1 python consumer

# terminal panel 3 (consumer1-3)
KAFKA_TOPIC=my-topic KAFKA_CONSUMER_GROUP_ID=my-topic-group-1 python consumer

# terminal panel 4 (consumer1-4)
KAFKA_TOPIC=my-topic KAFKA_CONSUMER_GROUP_ID=my-topic-group-1 python consumer
```

- Produce message through endpoint `/send-message`

```
url: http://localhost:8081/send-message
Method: POST
Body:
    {
        "topic": "my-topic",
        "value": "hello-world"  # message being produced to consumers
        // "partition": None  # specify partition receiving produced messages
    }
```
