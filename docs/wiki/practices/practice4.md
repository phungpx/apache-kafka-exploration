# Practice 3 - Brokers

- 3 brokers including Broker101, Broker102, Broker103
- 2 Topics: Topic-A (3 Partitions) and Topic-B (2 partitions)

| ![alt text](../../figures/practice4/topic-replication-factor2.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                                 _Figure 1._                                 |

- All produced messages will be broadcasted to all consumer groups and ensure each consumer groups will consume all produced messages.
- And each consumer groups, the mechanism of consuming messages is similar to [practice 2](./practice2.md)

## Docker Compose Setup

- Activate all crucial services with [dev.multiple-brokers.docker-compose.yml](../../../src/docker-compose/dev.multiple-brokers.docker-compose.yml)

```
docker compose -f src/docker-compose/dev.multiple-brokers.docker-compose.yml up
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
|                                 _Figure 2._                                 |

- Access `http://localhost:8000` to investigate a interesting mechanism of this setting.

| ![alt text](../../figures/practice4/topic-replication-factor6.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                             _Figure 3. Brokers_                             |

| ![alt text](../../figures/practice4/topic-replication-factor5.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                         _Figure 4. Consumer Groups_                         |

| ![alt text](../../figures/practice4/topic-replication-factor3.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                 _Figure 5. Topic-A Partitions Distribution_                 |

| ![alt text](../../figures/practice4/topic-replication-factor4.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                 _Figure 6. Topic-B Partitions Distribution_                 |
