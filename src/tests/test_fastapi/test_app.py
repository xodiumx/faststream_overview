import pytest
import pytest_asyncio
from fastapi.exceptions import RequestValidationError

from faststream.kafka import TestKafkaBroker

from settings import settings
from fast_stream.fastapi_integration.app import handler, publisher, router


@pytest_asyncio.fixture
async def broker():
    async with TestKafkaBroker(router.broker) as br:
        yield br


@pytest.mark.asyncio()
async def test_incorrect(broker):
    with pytest.raises(RequestValidationError):
        await broker.publish("user-id", settings.KAFKA_TOPIC_CONSUME)


@pytest.mark.asyncio()
async def test_handler(broker):
    user_id = 1

    await broker.publish(user_id, settings.KAFKA_TOPIC_CONSUME)

    handler.mock.assert_called_once_with(user_id)
    publisher.mock.assert_called_once_with(f"{user_id} created")
