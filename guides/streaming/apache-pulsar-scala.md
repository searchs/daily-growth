# Apache Pulsar with Scala

Consolidated from the historical `in-few-steps` repository.

This quickstart demonstrates the basic producer/consumer model for Apache Pulsar using Scala.

## Producer

```scala
import org.apache.pulsar.client.api._

object PulsarProducer {
  def main(args: Array[String]): Unit = {
    val client = PulsarClient.builder()
      .serviceUrl("pulsar://localhost:6650")
      .build()

    val producer = client.newProducer()
      .topic("my-topic")
      .create()

    try {
      (1 to 100).foreach { i =>
        producer.send(s"message-$i".getBytes())
      }
    } finally {
      producer.close()
      client.close()
    }
  }
}
```

## Consumer

```scala
import org.apache.pulsar.client.api._

object PulsarConsumer {
  def main(args: Array[String]): Unit = {
    val client = PulsarClient.builder()
      .serviceUrl("pulsar://localhost:6650")
      .build()

    val consumer = client.newConsumer()
      .topic("my-topic")
      .subscriptionName("my-subscription")
      .subscribe()

    try {
      while (true) {
        val msg = consumer.receive()
        println(new String(msg.getData))
        consumer.acknowledge(msg)
      }
    } finally {
      consumer.close()
      client.close()
    }
  }
}
```

For real systems, add explicit schema handling, error policies, dead-letter topics, observability and controlled shutdown.
