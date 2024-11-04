from granian.constants import Interfaces, Loops
from granian.server import Granian

from settings import settings


def get_server() -> Granian:
    return Granian(
        "fast_stream.custom.app:app",
        reload=settings.DEBUG,
        port=settings.SERVER_PORT,
        address=settings.SERVER_BIND,
        loop=Loops.uvloop,
        interface=Interfaces.ASGI,
        workers=settings.SERVER_WORKERS,
        threads=settings.SERVER_THREADS,
        log_access=settings.DEBUG,
    )


server = get_server()
