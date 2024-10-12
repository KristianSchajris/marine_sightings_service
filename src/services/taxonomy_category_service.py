# src/services/taxonomic_category_service.py
from src.models.taxonomic_category import TaxonomicCategory
from src.repositories.taxonomic_category_repository import TaxonomicCategoryRepository

class TaxonomicCategoryService:
    def __init__(self):
        self.repository = TaxonomicCategoryRepository()

    def create_taxonomic_category(self, kingdom: str, phylum: str, t_class: str, t_order: str, family: str, genus: str, specie_id: int) -> TaxonomicCategory:
        return self.repository.create(kingdom=kingdom, phylum=phylum, t_class=t_class, t_order=t_order, family=family, genus=genus, specie_id=specie_id)

    def get_taxonomic_category(self, category_id: int) -> TaxonomicCategory:
        return self.repository.get(category_id)

    def get_all_taxonomic_categories(self) -> list[TaxonomicCategory]:
        return self.repository.get_all()

    def update_taxonomic_category(self, category_id: int, kingdom: str, phylum: str, t_class: str, t_order: str, family: str, genus: str) -> TaxonomicCategory:
        return self.repository.update(category_id, kingdom=kingdom, phylum=phylum, t_class=t_class, t_order=t_order, family=family, genus=genus)

    def delete_taxonomic_category(self, category_id: int) -> bool:
        return self.repository.delete(category_id)
