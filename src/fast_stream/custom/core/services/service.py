from fast_stream.custom.core.entities.schemas import Data


class DataHandlerService:
    def __init__(self) -> None: ...

    async def processing(self, data: Data) -> "str":
        return "test"
