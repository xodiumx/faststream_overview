from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Base
    DEBUG: bool

    # Server
    SERVER_BIND: str
    SERVER_PORT: int
    SERVER_WORKERS: int
    SERVER_THREADS: int
    SERVER_TIMEOUT: int

    # Kafka
    KAFKA_HOST: str
    KAFKA_TOPIC_PRODUCE: str
    KAFKA_TOPIC_CONSUME: str


settings = Settings()
