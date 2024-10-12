# src/repositories/taxonomic_category_repository.py

from sqlmodel import Session
from src.models.taxonomic_category import TaxonomicCategory
from src.connect.db_connect import DatabaseConnet
from src.repositories.base.base_repository import BaseRepository

class TaxonomicCategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(DatabaseConnet())
    
    def create(self, kingdom: str, phylum: str, t_class: str, t_order: str, family: str, genus: str, specie_id: int):
        new_taxonomic_category = TaxonomicCategory(kingdom=kingdom, phylum=phylum, t_class=t_class, t_order=t_order, family=family, genus=genus, specie_id=specie_id)
        return super().create(new_taxonomic_category)

    def get(self, category_id: int):
        return super().get(TaxonomicCategory, category_id)
    
    def get_all(self):
        return super().get_all(TaxonomicCategory)

    def update(self, category_id: int, kingdom: str, phylum: str, t_class: str, t_order: str, family: str, genus: str, specie_id: int):
        category = self.get(category_id)
        if category:
            return super().update(category, kingdom=kingdom, phylum=phylum, t_class=t_class, t_order=t_order, family=family, genus=genus, specie_id=specie_id)
        return None

    def delete(self, category_id: int):
        category = self.get(category_id)
        if category:
            return super().delete(category)
        return False
