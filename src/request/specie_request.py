from pydantic import BaseModel

class SpecieRequest(BaseModel):
    common_name: str
    scientific_name: str
