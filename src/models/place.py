from sqlmodel import SQLModel, Field
from datetime import datetime

class Place(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name_place: str
    country: str
    state: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    
