from pydantic import BaseModel

class TaxonomicCategoryRequest(BaseModel):
    kingdom: str
    phylum: str
    t_class: str
    t_order: str
    family: str
    genus: str
    specie_id: int
