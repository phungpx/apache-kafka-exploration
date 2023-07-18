### 1.1 Case 1 - One consumer group (with two consumers) id and One producer (Development Mode)

- Acitvate all crucial services including kafka, kafka-ui, zookeeper

```
docker compose -f dev.docker-compose.yml up
```

- Producer with creating a topic name `my-topic` and `2` partitions

```
cd producer
```

```
# Activate virual environment
python -m venv .venv
source .venv/bin/activate

# Install all dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

```
chmod +x run.sh
KAFKA_TOPIC=my-topic KAFKA_TOPIC_PARTITIONS=2 KAFKA_REPLICATION_FACTOR=1 ./run.sh
```

- Run 2 different consumers in 2 different command pannels

```
cd consumer
```

```
# Activate virual environment
python -m venv .venv
source .venv/bin/activate

# Install all dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

```
# terminal pannel 1
cd consumer
KAFKA_TOPIC=my-topic KAFKA_CONSUMER_GROUP_ID=my-topic-group-1 KAFKA_TOPIC=my-topic python consumer

```

```
# terminal pannel 2
cd consumer
KAFKA_TOPIC=my-topic KAFKA_CONSUMER_GROUP_ID=my-topic-group-1 python consumer

```

- Produce message through endpoint `/send-message`

```
URL: http://localhost:8081/send-message
Method: POST
Body:
{
    "value": "testing-value"  (message being produced to consumers)
    // "partition": None  (specify partition receiving produced messages)
}
```

| Requested Body                      | Visualization                                                          |
| ----------------------------------- | ---------------------------------------------------------------------- |
| {value: string, partition: None}    | <img src="./figures/case-1-without-specific-parition.png" width="400"> |
| {value: string, partition: int = 1} | <img src="./figures/case-1-with-specific-partition.png" width="400">   |

| Send request (partition=None)                                 |
| ------------------------------------------------------------- |
| <img src="./figures/case-1-produce-messages.png" width="800"> |

| Consume messages (partition=None)                             |
| ------------------------------------------------------------- |
| <img src="./figures/case-1-consume-messages.png" width="800"> |

| Send request (partition=1)                                                |
| ------------------------------------------------------------------------- |
| <img src="./figures/case-1-produce-messages-partition-1.png" width="800"> |

| Consume messages (partition=1, online consumed by consumer which belongs to partition 1) |
| ---------------------------------------------------------------------------------------- |
| <img src="./figures/case-1-consume-messages-partition-1.png" width="800">                |

### 1.2 Case 1 - One consumer group (with two consumers) id and One producer (Production Mode)

- Run multiple docker compose files (https://stackoverflow.com/questions/62871280/should-i-have-multiple-docker-compose-files)

- Activate all crucial services

```
docker compose -f dev.docker-compose.yml up
```

- Run producer and consumers

```
docker compose -f case1.docker-compose.yml up
```

- Produce message through endpoint `/send-message`

```
URL: http://localhost:8081/send-message
Method: POST
Body:
{
    "value": "testing-value"  (message being produced to consumers)
    // "partition": None  (specify partition receiving produced messages)
}
```
