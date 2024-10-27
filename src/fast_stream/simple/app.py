from pydantic import BaseModel, Field, PositiveInt

from main import broker
from settings import settings


class User(BaseModel):
    user: str = Field(..., examples=["John"])
    user_id: PositiveInt = Field(..., examples=["1"])


@broker.subscriber(settings.KAFKA_TOPIC_CONSUME)
@broker.publisher(settings.KAFKA_TOPIC_PRODUCE)
async def handle_msg(data: User) -> str:
    return f"User: {data.user} - {data.user_id} registered"
