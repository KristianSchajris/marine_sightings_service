from fastapi.responses import JSONResponse

class JSONAdapter:
    def __init__(self, data: dict):
        self.data = data

    def get_response(self) -> JSONResponse:
        return JSONResponse(content=self.data)
