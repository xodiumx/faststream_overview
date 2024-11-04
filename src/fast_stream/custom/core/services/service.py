from fast_stream.custom.core.entities.schemas import Data


class DataHandlerService:
    def __init__(self) -> None: ...

    async def processing(self, data: Data) -> "str":
        """
        Some data processing
        """
        return f"Data received - {data.person.first_name} - {data.person.phone} - {data.address.city.name}"
