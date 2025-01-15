from __future__ import annotations

import click

from nox.domains.kafka_manager import KafkaManager

# Initialize Kafka manager
kafka_manager = KafkaManager()


@click.group()
def kafka():
    """Kafka management commands."""
    pass


@click.command()
@click.option('--topic', required=True, help='Kafka topic to produce the message to')
@click.option('--message', required=True, help='Message to produce to the topic')
def produce(topic, message):
    """Produce a message to a Kafka topic."""
    result = kafka_manager.produce_message(topic, message)
    click.echo(result)


@click.command()
@click.option('--topic', required=True, help='Kafka topic to consume messages from')
@click.option('--group-id', required=True, help='Consumer group ID')
@click.option('--auto-offset-reset', default='earliest', type=click.Choice(['earliest', 'latest']), help='Offset reset policy')
def consume(topic, group_id, auto_offset_reset):
    """Consume messages from a Kafka topic."""
    messages = kafka_manager.consume_messages(topic, group_id, auto_offset_reset)
    click.echo('\n'.join(messages))


@click.command()
def list_topics():
    """List all Kafka topics."""
    topics = kafka_manager.list_topics()
    click.echo('\n'.join(topics))


@click.command()
@click.option('--name', required=True, help='Name of the topic to create')
@click.option('--partitions', default=1, help='Number of partitions for the topic')
@click.option('--replication-factor', default=1, help='Replication factor for the topic')
def create_topic(name, partitions, replication_factor):
    """Create a new Kafka topic."""
    result = kafka_manager.create_topic(name, partitions, replication_factor)
    click.echo(result)


@click.command()
@click.option('--name', required=True, help='Name of the topic to delete')
def delete_topic(name):
    """Delete a Kafka topic."""
    result = kafka_manager.delete_topic(name)
    click.echo(result)


# Add commands to the kafka group
kafka.add_command(produce)
kafka.add_command(consume)
kafka.add_command(list_topics)
kafka.add_command(create_topic)
kafka.add_command(delete_topic)
