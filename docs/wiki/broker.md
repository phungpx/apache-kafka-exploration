# Broker

- A kafka cluster is composed of multiple brokers (servers).
- Each broker is identified with its ID (which is an `integer`) Eg. broker 101, broker 102, broker 103,...
- Each broker contains certain topic partitions --> this means that your data is going to `be distributed across all brokers`.
- After connecting to any broker (called a bootstrap broker), you will be connected or know how to the entire cluster (because kafka clients have smart mechanics for that).

## 1. Brokers and topics

Example of `Topic A` with `3 partitions` and `Topic B` with `2 partitions`.

|            ![alt text](../figures/broker/brokers-1.png?raw=true)             |
| :--------------------------------------------------------------------------: |
| _Figure 1: An example of distribution of paritions to brokers in a cluster._ |

In this example, the data and partitions is going to be distributed across all brokers, and this is what makes kafka scale, and what's actually called horizontal scaling. Because the more partitions and be more brokers we add, the more data is going to be spread out across our entire cluster.

## 2. Kafka Broker Discovery

- Every Kafka broker is also called a `bootstrap server`.
- That means that you only need to connect to one broker, and the Kafka clients will know how to be connected to the entire cluster (smart clients).

| ![alt text](../figures/broker/brokers-2.png?raw=true) |
| :---------------------------------------------------: |
|  _Figure 2: An example of connection to a cluster._   |

_So that means in this cluster, we only need to connect to one broker and then clients know how to be connected to the entire cluster. So our Kafka client is going to initiate a connection into Broker 101, as well as a metadata request. And then the Broker 101, if successful, is going to return the list of all the brokers in the cluster, and actually more data as well, such as which broker has which partition. And then the Kafka client is, thanks to this list of all brokers, going to be able to connect to the broker it needs, for example to produce or to consume data. So that means that each broker in your Kafka cluster is pretty smart and it knows about all the other brokers, all the topics, and all the partitions. That means that each broker has all the metadata information._
