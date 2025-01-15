from __future__ import annotations

from confluent_kafka import Consumer
from confluent_kafka import KafkaError
from confluent_kafka import KafkaException
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient
from confluent_kafka.admin import NewTopic


class KafkaManager:
    def __init__(self, bootstrap_servers: str = 'localhost:9092'):
        """Initialize the Kafka manager with the specified bootstrap servers."""
        self.bootstrap_servers = bootstrap_servers
        self.producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        self.admin_client = AdminClient({'bootstrap.servers': self.bootstrap_servers})

    def produce_message(self, topic: str, message: str) -> str:
        """Produce a message to a Kafka topic."""
        try:
            self.producer.produce(topic, message)
            self.producer.flush()
            return f"Message sent to topic '{topic}'."
        except KafkaException as e:
            return f"Error producing message: {str(e)}"

    def consume_messages(self, topic: str, group_id: str, auto_offset_reset: str = 'earliest') -> list:
        """Consume messages from a Kafka topic."""
        try:
            consumer = Consumer({
                'bootstrap.servers': self.bootstrap_servers,
                'group.id': group_id,
                'auto.offset.reset': auto_offset_reset,
            })
            consumer.subscribe([topic])
            messages = []

            for _ in range(10):  # Adjust the number of messages to consume
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        raise KafkaException(msg.error())
                messages.append(msg.value().decode('utf-8'))

            consumer.close()
            return messages
        except KafkaException as e:
            return [f"Error consuming messages: {str(e)}"]

    def list_topics(self) -> list:
        """List all Kafka topics."""
        try:
            topics = self.admin_client.list_topics(timeout=10).topics
            return list(topics.keys())
        except KafkaException as e:
            return [f"Error listing topics: {str(e)}"]

    def create_topic(self, topic_name: str, num_partitions: int = 1, replication_factor: int = 1) -> str:
        """Create a new Kafka topic."""
        try:
            new_topic = NewTopic(topic_name, num_partitions, replication_factor)
            self.admin_client.create_topics([new_topic])
            return f"Topic '{topic_name}' created successfully."
        except KafkaException as e:
            return f"Error creating topic '{topic_name}': {str(e)}"

    def delete_topic(self, topic_name: str) -> str:
        """Delete a Kafka topic."""
        try:
            self.admin_client.delete_topics([topic_name])
            return f"Topic '{topic_name}' deleted successfully."
        except KafkaException as e:
            return f"Error deleting topic '{topic_name}': {str(e)}"
