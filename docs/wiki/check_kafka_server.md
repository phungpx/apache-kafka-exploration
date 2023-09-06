1. Create kafka topic

```bash
bin/kafka-topics.sh --create --bootstrap-server <Eg. localhost:9091> --topic <name-of-topic> --partitions <num-partitions> --replication-factor <num-replication-factor>
```

2. Check kafka topics

```bash
bin/kafka-topics.sh --bootstrap-server <Eg. localhost:9091> --describe
```

3. Check kafka topic

```bash
bin/kafka-topics.sh --bootstrap-server <Eg. localhost:9091> --describe --topic <name-of-topic>
```
