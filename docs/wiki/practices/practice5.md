# Practice 5 - Topic Replication Factor

| ![alt text](../../figures/practice5/topic_replication_factor1.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                                 _Figure 1._                                 |

| ![alt text](../../figures/practice5/topic_replication_factor7.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                                 _Figure 2._                                 |

## Docker Compose Setup

- Activate all crucial services with [dev.practice-5.docker-compose.yml](../../../src/docker-compose/dev.practice-5.docker-compose.yml)

```
docker compose -f src/docker-compose/dev.practice-5.docker-compose.yml up
```

- Run producer and consumers with [practice-5.docker-compose.yml](../../../src/docker-compose/practice-5.docker-compose.yml)

```
docker compose -f src/docker-compose/practice-5.docker-compose.yml up
```

- Produce messages (with/without specific partition) through endpoint `/send-message` to examine all scenarios which I've discussed above.

```
URL: http://localhost:8081/send-message
Method: POST
Body:
    {
        "topic": "topic-A",
        "value": "practice-5"  # message being produced to consumers
        // "partition": None  # specify partition receiving produced messages
    }
```

- Logs all consumers after producing a ton of messages to all consumer groups by using `docker logs -f <container-name>`

| ![alt text](../../figures/practice5/topic_replication_factor5.png?raw=true) |
| :-------------------------------------------------------------------------: |
|                                 _Figure 3._                                 |

- Access `http://localhost:8000` to investigate a interesting mechanism of this setting.

|                                            ![alt text](../../figures/practice5/topic_replication_factor2.png?raw=true)                                             |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| _Figure 4. Distribution of partitions in brokers, in this case, Broker 101 is Leader for Partition 0 (Topic-A) and Broker 103 is Leader for Partition 1 (Topic-A)_ |

- Remove Broker 101: `docker stop broker101`

|                         ![alt text](../../figures/practice5/topic_replication_factor6.png?raw=true)                          |
| :--------------------------------------------------------------------------------------------------------------------------: |
| _Figure 5. Broker 103 becomes the Leader for Partition 0 (Topic-A) and Broker 103 is still Leader for Partition 1 (Topic-A)_ |
