"""
Simple example for data generate
"""

import time
import random

from faker import Faker

from confluent_kafka import Producer
from confluent_kafka.cimpl import Message
from faststream import Logger

from settings import settings
from fast_stream.custom.core.entities.schemas import Data, AddressInfo, Person, City

LOCAL_SERVER_ID: int = 0

fake = Faker()
logger = Logger(__name__, 10)


def delivery_report(err, msg: Message) -> None:
    if err is not None:
        logger.error(f"Message delivery failed: {err}")
    else:
        logger.info(f"Message {msg.value()} delivered to: \ntopic - {msg.topic()} \npartition - [{msg.partition()}]")


def produce_messages() -> None:
    """
    Infinite data generation
    """
    producer = Producer({"bootstrap.servers": settings.KAFKA_HOST})
    while True:
        data = Data(
            id=str(fake.uuid4()),
            name=fake.user_name(),
            description=fake.text(),
            address=AddressInfo(
                name=fake.address(),
                city=City(
                    name=fake.city(),
                    country=fake.country(),
                ),
            ),
            person=Person(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                company=fake.company(),
            ),
        )
        json_data = data.model_dump_json()
        producer.poll(0)
        producer.produce(settings.KAFKA_TOPIC_CONSUME, json_data, callback=delivery_report)
        logger.warning(f"Data generated {json_data}")
        time.sleep(random.random())


if __name__ == "__main__":
    produce_messages()
