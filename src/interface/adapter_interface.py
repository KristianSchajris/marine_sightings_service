from fastapi.responses import JSONResponse
from abc import ABC, abstractmethod

class AdapterInterface(ABC):

    @abstractmethod
    def get_response(self) -> JSONResponse:
        pass
