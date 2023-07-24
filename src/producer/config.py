import os


def str2bool(s: str):
    s = s.lower()
    if s in ("yes", "y", "1", "true", "t", "on"):
        return True
    if s in ("no", "n", "0", "false", "f", "off"):
        return False
    raise ValueError("invalid truth value %r" % (s,))


class Config:
    # Logging Setting
    LOG_FOLDER = "logging"
    LOG_NAME = "producer"

    # Kafka Producer Setting
    KAFKA_SERVERS = os.getenv("KAFKA_SERVERS", "localhost:29092")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "my-topic")
    KAFKA_TOPIC_PARTITIONS = os.getenv("KAFKA_TOPIC_PARTITIONS", 3)
    KAFKA_REPLICATION_FACTOR = os.getenv("KAFKA_REPLICATION_FACTOR", 1)
    KAFKA_BATCH_SIZE = os.getenv("KAFKA_BATCH_SIZE", 16384)  # https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html#batch-size

    # Set message keys
    MESSAGE_KEYS_RANDOM = str2bool(os.getenv("MESSAGE_KEYS_RANDOM", "false"))
