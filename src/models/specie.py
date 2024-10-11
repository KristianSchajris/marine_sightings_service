from sqlmodel import SQLModel, Field
from datetime import datetime

class Specie(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    common_name: str
    scientific_name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
