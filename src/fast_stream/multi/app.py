from prometheus_client import CollectorRegistry, make_asgi_app
from faststream.annotations import Logger
from faststream.kafka import KafkaBroker
from faststream.asgi import AsgiFastStream, make_ping_asgi

from settings import settings

registry = CollectorRegistry()
broker = KafkaBroker(settings.KAFKA_HOST)
app = AsgiFastStream(
    broker, asgi_routes=[("/metrics", make_asgi_app(registry)), ("/health", make_ping_asgi(broker, timeout=3))]
)


@broker.subscriber("test-queue")
@broker.publisher("response-queue")
@broker.subscriber("another-queue")
@broker.publisher("another-response-queue")
async def handle(msg, logger: Logger):
    logger.info(msg)
    return "Response"


@broker.subscriber("response-queue")
async def handle_response_1(msg, logger: Logger):
    logger.info(msg)


@broker.subscriber("another-response-queue")
async def handle_response_2(msg, logger: Logger):
    logger.info(msg)


@app.after_startup
async def test():
    await broker.publish("Hello!", "test-queue")
    await broker.publish("Hello!", "another-queue")
