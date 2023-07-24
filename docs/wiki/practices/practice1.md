# Practice 1

- Run all services

```
docker compose -f src/docker-compose/practice-1.docker-compose.yml up
```

- Produce messages through endpoint `/send-message`

```
URL: http://localhost:8081/send-message
Method: POST
Body:
    {
        "topic": "my-topic",
        "value": "testing-value",
        // "partition": None
    }
```
