from prometheus_client import CollectorRegistry, make_asgi_app
from faststream.asgi import AsgiFastStream, make_ping_asgi
from faststream.kafka import KafkaBroker
from faststream.kafka.prometheus import KafkaPrometheusMiddleware

from settings import settings
from fast_stream.custom.core.services.handlers import handler_router


registry = CollectorRegistry()
broker = KafkaBroker(settings.KAFKA_HOST, middlewares=(KafkaPrometheusMiddleware(registry=registry),))
broker.include_router(handler_router)
app = AsgiFastStream(
    broker,
    asgi_routes=[("/metrics", make_asgi_app(registry)), ("/health", make_ping_asgi(broker, timeout=3))],
    asyncapi_path="/docs",
)
