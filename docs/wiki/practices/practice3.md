# Practice 3

- Having three consumer group consumers and one broker with 3 partitions.

| ![alt text](../../figures/consumer_group/multiple-consumers-in-a-group.png?raw=true) |
| :----------------------------------------------------------------------------------: |
|                 _Figure 1: An example of multiple Consumer Groups._                  |

- All produced messages will be broadcasted to all consumer groups and ensure each consumer groups will consume all produced messages.
- And each consumer groups, the mechanism of consuming messages is similar to [practice 2](./practice2.md)

## Docker Compose Setup

- Activate all crucial services with [dev.docker-compose.yml](../../../src/docker-compose/dev.docker-compose.yml)

```
docker compose -f dev.docker-compose.yml up
```

- Run producer and consumers with [practice3.docker-compose.yml](../../../src/docker-compose/practice-3.docker-compose.yml)

```
docker compose -f practice3.docker-compose.yml up
```

- Produce messages (with/without specific partition) through endpoint `/send-message` to examine all scenarios which I've discussed above.

```
URL: http://localhost:8081/send-message
Method: POST
Body:
    {
        "value": "testing-value"  (message being produced to consumers)
        // "partition": None  (specify partition receiving produced messages)
    }
```
