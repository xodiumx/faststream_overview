from faststream import Depends
from faststream.kafka import KafkaRouter
from faststream.annotations import Logger

from settings import settings
from fast_stream.custom.core.entities.schemas import Data

from .service import DataHandlerService

handler_router = KafkaRouter()


@handler_router.publisher(
    settings.KAFKA_TOPIC_PRODUCE, key=b"handler", title="Handler_pub", description="Handler producer description"
)
@handler_router.subscriber(
    settings.KAFKA_TOPIC_CONSUME, title="Handler_sub", description="Handler consumer description"
)
async def handle_data(data: Data, logger: Logger, service: DataHandlerService = Depends(DataHandlerService)) -> str:
    try:
        result = await service.processing(data=data)
    except Exception:
        result = f"Processing error on {data.id}"
        logger.exception("Data processing error")
    else:
        logger.info("Data successfully processed")
    return result
