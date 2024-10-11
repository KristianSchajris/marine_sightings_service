from pydantic import BaseModel

class SightingRequest(BaseModel):
    latitude: float
    longitude: float
    image_sighting: str = None
    notes: str
    place_id: int
    specie_id: int
    user_id: int  # Ajustar según tu modelo de usuario
