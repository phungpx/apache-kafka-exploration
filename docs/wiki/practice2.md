### 2 Case 2 - Two consumer groups (group 1 - 3 partitions and group 2- 1 parititon)

- Activate all crucial services

```
docker compose -f dev.docker-compose.yml up
```

- Run producer and consumers

```
docker compose -f case2.docker-compose.yml up
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

| Visualization (partition=None)                             |
| ---------------------------------------------------------- |
| <img src="./figures/case-2-visualization.png" width="800"> |

| Consume messages (partition=None)                             |
| ------------------------------------------------------------- |
| <img src="./figures/case-2-consume-messages.png" width="800"> |
