# Producer

- Producers write data to topics (which are made of partitions).
- Producers know which partition to write to (and which kafka broker has it).
- In case of Kafka broker failures, Producers will `automatically recover`.
