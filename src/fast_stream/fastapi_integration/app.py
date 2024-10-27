from fastapi import FastAPI
from faststream.kafka.fastapi import Logger, KafkaRouter

from settings import settings

router = KafkaRouter(settings.KAFKA_HOST)
app = FastAPI(lifespan=router.lifespan_context)
publisher = router.publisher(settings.KAFKA_TOPIC_PRODUCE)


@publisher
@router.subscriber(settings.KAFKA_TOPIC_CONSUME)
async def handler(user_id: int, logger: Logger) -> str:
    logger.info(user_id)
    return f"{user_id} created"


app.include_router(router)
