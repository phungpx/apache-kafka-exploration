# Topics, Partitions, and Offsets

## 1. Kafka Topics

- Topics: a particular stream of data with the kafka cluster.
- Like a table in a database (without all the constraints).
- You can have as many topics as you want.
- A topic is identified by its name.
- Support any kind of message formats (you can send json, avro, binary, text file,...).
- The sequence of messages is called a data stream
- You cannot QUERY topics, instead, use Kafka Producers to send data and Kafka Consumers to read the data.

## 2. Partitions and Offsets

- Topics are split in PARTITIONS (example: 100 partitions)
  - Messages within each partition are ordered.
  - Each message within a partition gets an incremental id, called OFFSET.
- Kafka topics are immutable: once data is written to a partition, it cannot be changed.

## 3. Topic Example

## 4. Important Notes

- Once the data is written to a partition, it cannot be changed `(immutability)`.
- Data is kept only for a limited time (default is one week - configurable).
- Offset only has a meaning for a specific partition.
  - E.g offset 3 in partition 0 doesn’t represent the same data as offset 3 in parition1.
  - Offsets are not reused even if previous messages have been deleted.
- Order is guaranteed only within a partition (not across partitions).
- Data is assigned randomly to a partition unless a key is provided (more on this later).
- You can have as many partitions per topic as you want.
