# Topic Replication Factor

- Topic should have a replication factor > 1 (usually between 2 and 3).
- This way if a broker is down (for maintenance or for a technical issue), another broker still has a copy of the data to serve and receive.
- Example: Topic-A with 2 partitions and replication factor of 2, and we have 3 Kafka brokers.
  we're going to place partition-0 of Topic-A onto broker 101, partition-1 of Topic-A onto broker 102. And then because we have a replication factor of 2, then we’re going to have a topic of partition-0 onto broker 102 with a replication mechanism, and a copy of partition-1 onto broker 103 with a replication mechanism.

| ![alt text](../figures/topic_replication_factor/topic_replication_factor1.png?raw=true) |
| :-------------------------------------------------------------------------------------: |
|                _Figure 1: An example of using topic replication factor._                |

- Example: we lose Broker 102 - Result: Broker 101 and 103 can still serve the data

| ![alt text](../figures/topic_replication_factor/topic_replication_factor2.png?raw=true) |
| :-------------------------------------------------------------------------------------: |
|                   _Figure 2: An example of any broker being downed._                    |

## 1. Concept of Leader for a Partition

- At any time only ONE broker can be a leader for a given partition.
- Producers can only send data to the broker that is the leader of a partition.
- Example: Broker 101 is the leader of Partition 0, and Broker 102 is the leader of Partition 1.
  Add a little star on the leader of each partition. As you can see, broker 101 is the leader of partition-0, and broker 102 is the leader of partition-1, but broker 102 is a replica of partition zero, and broker 103 is a replica of partition-0. So the other brokers replicate the data. And if the data is replicated fast enough, and each replica is going to be called the ISR (in-sync replica), so if the data is replicated well, then they are synchronized in terms of the data replication.

| ![alt text](../figures/topic_replication_factor/topic_replication_factor3.png?raw=true) |
| :-------------------------------------------------------------------------------------: |
|                    _Figure 3: An example of leaders for partitions._                    |

- The other broker will replicate the data.
- Therefore, each partition has one leader and multiple ISR (in-sync replica).

## 2. Default producer & consumer behavior with leaders

- Kafka Producers can only write to the leader broker for a partition.
- Kafka Consumers by default will read from the leader broker for a partition.

| ![alt text](../figures/topic_replication_factor/topic_replication_factor4.png?raw=true) |
| :-------------------------------------------------------------------------------------: |
|                                       _Figure 4._                                       |

## 3. Kafka Consumers Replica Fetching (Kafka v2.4+)

- Since Kafka 2.4, it is possible to configure consumers to read from the closest replica.
- This may help improve latency, and also decrease network costs if using the cloud.

| ![alt text](../figures/topic_replication_factor/topic_replication_factor5.png?raw=true) |
| :-------------------------------------------------------------------------------------: |
|                                       _Figure 5._                                       |
