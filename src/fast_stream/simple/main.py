# from faststream.rabbit import RabbitBroker
# from faststream.nats import NatsBroker
# from faststream.redis import RedisBroker
# broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
# broker = NatsBroker("nats://localhost:4222/")
# broker = RedisBroker("redis://localhost:6379/")

from prometheus_client import CollectorRegistry, make_asgi_app
from faststream.asgi import AsgiFastStream, make_ping_asgi
from faststream.kafka import KafkaBroker
from faststream.kafka.prometheus import KafkaPrometheusMiddleware

from settings import settings


registry = CollectorRegistry()
broker = KafkaBroker(settings.KAFKA_HOST, middlewares=(KafkaPrometheusMiddleware(registry=registry),))
app = AsgiFastStream(
    broker, asgi_routes=[("/metrics", make_asgi_app(registry)), ("/health", make_ping_asgi(broker, timeout=3))]
)
