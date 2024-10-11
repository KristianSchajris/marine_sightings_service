from sqlmodel import SQLModel, Field
from datetime import datetime

class TaxonomicCategory(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    kingdom: str
    phylum: str
    t_class: str
    t_order: str
    family: str
    genus: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    specie_id: int = Field(foreign_key="specie.id")
