import asyncio
from typing import Annotated

from fastapi import FastAPI, Depends
from faststream.kafka.fastapi import Logger, KafkaRouter, KafkaBroker

from settings import settings

app = FastAPI()
router = KafkaRouter(settings.KAFKA_HOST)


def broker() -> KafkaBroker:
    return router.broker


async def test_sleep(time: int, logger: Logger) -> None:
    await asyncio.sleep(time)
    logger.info("Sleep ended")


@router.subscriber(settings.KAFKA_TOPIC_CONSUME)
@router.publisher(settings.KAFKA_TOPIC_PRODUCE)
async def handler(logger: Logger) -> str:
    await test_sleep(10, logger=logger)
    return "Message consumed in faststream handler"


@router.get("/")
async def base_route(broker: Annotated[KafkaBroker, Depends(broker)]):
    await broker.publish("Test consume message", settings.KAFKA_TOPIC_CONSUME)
    return "Test HTTP"


app.include_router(router)
