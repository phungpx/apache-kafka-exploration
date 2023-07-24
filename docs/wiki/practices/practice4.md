# Broker

- A kafka cluster is composed of multiple brokers (servers).
- Each broker is identified with its ID (which is an `integer`) Eg. broker 101, broker 102, broker 103,...
- Each broker contains certain topic partitions --> this means that your data is going to `be distributed across all brokers`.
- After connecting to any broker (called a bootstrap broker), you will be connected or know how to the entire cluster (because kafka clients have smart mechanics for that).

## 1. Brokers and topics

Example of `Topic A` with `3 partitions` and `Topic B` with `2 partitions`.

|           ![alt text](../../figures/broker/brokers-1.png?raw=true)           |
| :--------------------------------------------------------------------------: |
| _Figure 1: An example of distribution of paritions to brokers in a cluster._ |

In this example, the data and partitions is going to be distributed across all brokers, and this is what makes kafka scale, and what's actually called horizontal scaling. Because the more partitions and be more brokers we add, the more data is going to be spread out across our entire cluster.

## 2. Kafka Broker Discovery

- Every Kafka broker is also called a `bootstrap server`.
- That means that you only need to connect to one broker, and the Kafka clients will know how to be connected to the entire cluster (smart clients).

| ![alt text](../../figures/broker/brokers-2.png?raw=true) |
| :------------------------------------------------------: |
|    _Figure 2: An example of connection to a cluster._    |

_So that means in this cluster, we only need to connect to one broker and then clients know how to be connected to the entire cluster. So our Kafka client is going to initiate a connection into Broker 101, as well as a metadata request. And then the Broker 101, if successful, is going to return the list of all the brokers in the cluster, and actually more data as well, such as which broker has which partition. And then the Kafka client is, thanks to this list of all brokers, going to be able to connect to the broker it needs, for example to produce or to consume data. So that means that each broker in your Kafka cluster is pretty smart and it knows about all the other brokers, all the topics, and all the partitions. That means that each broker has all the metadata information._

## 3. Practice 4 - Brokers

- This practice aims to dive deeper into some tough theory about [`broker`](../broker.md) and comprehend the mechanism of partitions distributed across all brokers as well as producing & consuming messages among consumer groups.
- 3 brokers including Broker101, Broker102, Broker103
- 2 Topics: Topic-A (3 Partitions) and Topic-B (2 partitions)

| ![alt text](../../figures/practice4/topic-replication-factor2.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                                 _Figure 3._                                 |

- All produced messages will be broadcasted to all consumer groups and ensure each consumer groups will consume all produced messages of corresponding topic.
- And each consumer groups, the mechanism of consuming messages is similar to [practice 2](./practice2.md)

## Docker Compose Setup

- Activate all crucial services with [dev.practice-4.docker-compose.yml](../../../src/docker-compose/dev.practice-4.docker-compose.yml)

```
docker compose -f src/docker-compose/dev.practice-4.docker-compose.yml up
```

- Run producer and consumers with [practice-4.docker-compose.yml](../../../src/docker-compose/practice-4.docker-compose.yml)

```
docker compose -f src/docker-compose/practice-4.docker-compose.yml up
```

- Produce messages (with/without specific partition) through endpoint `/send-message` to examine all scenarios which I've discussed above.

```
URL: http://localhost:8081/send-message
Method: POST
Body:
    {
        "topic": "topic-A", # or "topic-B"
        "value": "testing-value"  # message being produced to consumers
        // "partition": None  # specify partition receiving produced messages
    }
```

- Logs all consumers after producing a ton of messages to all consumer groups by using `docker logs -f <container-name>`

| ![alt text](../../figures/practice4/topic-replication-factor1.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                                 _Figure 4._                                 |

- Access `http://localhost:8000` to investigate a interesting mechanism of this setting.

| ![alt text](../../figures/practice4/topic-replication-factor6.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                             _Figure 5. Brokers_                             |

| ![alt text](../../figures/practice4/topic-replication-factor5.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                         _Figure 6. Consumer Groups_                         |

| ![alt text](../../figures/practice4/topic-replication-factor3.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                 _Figure 7. Topic-A Partitions Distribution_                 |

| ![alt text](../../figures/practice4/topic-replication-factor4.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                 _Figure 8. Topic-B Partitions Distribution_                 |
