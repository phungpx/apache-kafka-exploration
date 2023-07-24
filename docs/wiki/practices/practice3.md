# Consumer Groups

- All the consumers in an application read data as a consumer group.

- Each consumer within a group reads from exclusive partitions.

| ![alt text](../../figures/consumer_group/consumer-group-example.png?raw=true) |
| :---------------------------------------------------------------------------: |
|                   _Figure 1: An example of Consumer Group._                   |

## 1. Multiple Consumer Groups in one topic?

- In Apache Kafka it is acceptable to have multiple consumer groups on the same topic.

- To create distinct consumer group, use the consumer property `group.id`

```
# Kafka Consumer
consumer = Consumer({
    'bootstrap.servers': Config.KAFKA_SERVERS,
    'group.id': Config.KAFKA_CONSUMER_GROUP_ID,
    'auto.offset.reset': 'earliest'
})
```

| ![alt text](../../figures/consumer_group/multiple-consumers-in-a-group.png?raw=true) |
| :----------------------------------------------------------------------------------: |
|                 _Figure 2: An example of multiple Consumer Groups._                  |

## 2. Practice 3

- Having three consumer group consumers and one broker with 3 partitions.

| ![alt text](../../figures/consumer_group/multiple-consumers-in-a-group.png?raw=true) |
| :----------------------------------------------------------------------------------: |
|                 _Figure 3: An example of multiple Consumer Groups._                  |

- All produced messages will be broadcasted to all consumer groups and ensure each consumer groups will consume all produced messages.
- And each consumer groups, the mechanism of consuming messages is similar to [practice 2](./practice2.md)

### Usage

- Activate all crucial services with [dev.docker-compose.yml](../../../src/docker-compose/dev.docker-compose.yml)

```
docker compose -f src/docker-compose/dev.docker-compose.yml up
```

- Run producer and consumers with [practice-3.docker-compose.yml](../../../src/docker-compose/practice-3.docker-compose.yml)

```
docker compose -f src/docker-compose/practice-3.docker-compose.yml up
```

- Logs all consumers before producing a ton of messages to all consumer groups by using `docker logs -f <container-name>`

| ![alt text](../../figures/practice3/practice-3-logs-before.png?raw=true) |
| :----------------------------------------------------------------------: |
|              _Figure 4: Logs of multiple Consumer Groups._               |

- Produce messages (with/without specific partition) through endpoint `/send-message` to examine all scenarios which I've discussed above.

```
URL: http://localhost:8081/send-message
Method: POST
Body:
    {
        "topic": "my-topic",
        "value": "testing-value"  # message being produced to consumers
        // "partition": None  # specify partition receiving produced messages
    }
```

- Logs all consumers after producing a ton of messages to all consumer groups by using `docker logs -f <container-name>`

| ![alt text](../../figures/practice3/practice-3-logs-after.png?raw=true) |
| :---------------------------------------------------------------------: |
|              _Figure 5: Logs of multiple Consumer Groups._              |
