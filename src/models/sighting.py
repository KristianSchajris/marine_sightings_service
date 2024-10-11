from sqlmodel import SQLModel, Field
from datetime import datetime

class Sighting(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    latitude: float
    longitude: float
    image_sighting: str = None
    notes: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    place_id: int = Field(foreign_key="place.id")
    specie_id: int = Field(foreign_key="specie.id")
    user_id: int  # Ajustar según tu modelo de usuario
