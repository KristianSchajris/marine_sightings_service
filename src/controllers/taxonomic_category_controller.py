from src.models.taxonomic_category import TaxonomicCategory
from src.services.taxonomy_category_service import TaxonomicCategoryService

class TaxonomicCategoryController:
    def __init__(self):
        self.service = TaxonomicCategoryService()

    def create_taxonomic_category(self, kingdom: str, phylum: str, t_class: str, t_order: str, family: str, genus: str, specie_id: int) -> TaxonomicCategory:
        return self.service.create_taxonomic_category(kingdom=kingdom, phylum=phylum, t_class=t_class, t_order=t_order, family=family, genus=genus, specie_id=specie_id)

    def get_taxonomic_category(self, category_id: int) -> TaxonomicCategory:
        return self.service.get_taxonomic_category(category_id)

    def get_all_taxonomic_categories(self) -> list[TaxonomicCategory]:
        return self.service.get_all_taxonomic_categories()

    def update_taxonomic_category(self, category_id: int, kingdom: str, phylum: str, t_class: str, t_order: str, family: str, genus: str) -> TaxonomicCategory:
        return self.service.update_taxonomic_category(category_id, kingdom=kingdom, phylum=phylum, t_class=t_class, t_order=t_order, family=family, genus=genus)

    def delete_taxonomic_category(self, category_id: int) -> bool:
        return self.service.delete_taxonomic_category(category_id)
