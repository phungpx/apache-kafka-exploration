# Consumer Groups

- All the consumers in an application read data as a consumer group.

- Each consumer within a group reads from exclusive partitions.

| ![alt text](../figures/consumer_group/consumer-group-example.png?raw=true) |
| :------------------------------------------------------------------------: |
|                 _Figure 1: An example of Consumer Group._                  |

## 1. What if too many consumers?

- If you have more consumers than partitions, some consumers will be INACTIVE. (=> num_partitions >= num_consumers in the same group)

| ![alt text](../figures/consumer_group/consumer-group-example.png?raw=true) |
| :------------------------------------------------------------------------: |
|   _Figure 2: An example of an inactivate consumer in a consumer group._    |

## 2. Multiple Consumer Groups in one topic?

- In Apache Kafka it is acceptable to have multiple consumer groups on the same topic.

- To create distinct consumer group, use the consumer property `group.id`

```
# Kafka Consumer
consumer = Consumer({
    'bootstrap.servers': Config.KAFKA_SERVERS,
    'group.id': Config.KAFKA_CONSUMER_GROUP_ID,
    'auto.offset.reset': 'earliest'
})
```

| ![alt text](../figures/consumer_group/consumer-group-example.png?raw=true) |
| :------------------------------------------------------------------------: |
|            _Figure 3: An example of multiple Consumer Groups._             |

## 3. Consumer Offsets

- Kafka stores the offsets at which a consumer group has been reading.

- The offsets committed are in Kafka topic name `__consumer_offsets`.

- When `a consumer in a group` has processed data received from Kafka, it should be `periodically committing the offsets` (the kafka broker will write to `__consumer_offsets`, not the group itself).

|  ![alt text](../figures/consumer_group/consumer-group-example.png?raw=true)  |
| :--------------------------------------------------------------------------: |
| _Figure 4: An example of Committing offsets and reads messages from broker._ |

- If a consumer dies, it will be able to read back from where it left off thanks to the committed consumer offsets!.

## 4. Delivery semantics for consumers

- By default, Java Consumer will automatically commit offset (at least once).
- There are 3 delivery semantics if you choose to commit manually.
  - `At least once (usually preferred)`
    - Offsets are committed after the message is processed.
    - If the processing goes wrong, the message will be read again.
    - This can result in duplicate processing of messages. Make sure your processing is idempotent (i.e. processing again the messages won't impact on your systems)
  - `At most once`
    - Offsets are committed as soon as messages are received.
    - If the processing goes wrong, some messages will be lost (they won't be read again.)
  - `Exactly once`
    - For kafka => kafka workflow: use the Transactional API (easy with Kafka Streams API).
    - For kafka => External System workflows: use an idempotent consumer.
