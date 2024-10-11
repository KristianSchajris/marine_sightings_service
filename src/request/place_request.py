from pydantic import BaseModel

class PlaceRequest(BaseModel):
    name_place: str
    country: str
    state: str
