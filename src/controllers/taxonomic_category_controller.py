from sqlmodel import Session
from src.models.taxonomic_category import TaxonomicCategory
from src.connect.db_connect import Database

class TaxonomicCategoryController:
    def __init__(self):
        self.db = Database()

    def create_taxonomic_category(self, kingdom: str, phylum: str, t_class: str, t_order: str, family: str, genus: str, specie_id: int):
        with self.db.get_session() as session:
            new_category = TaxonomicCategory(kingdom=kingdom, phylum=phylum, t_class=t_class, t_order=t_order, family=family, genus=genus, specie_id=specie_id)
            session.add(new_category)
            session.commit()
            session.refresh(new_category)
            return new_category

    def get_taxonomic_category(self, category_id: int):
        with self.db.get_session() as session:
            return session.get(TaxonomicCategory, category_id)
    
    def get_all_taxonomic_categories(self):
        with self.db.get_session() as session:
            return session.query(TaxonomicCategory).all()

    def update_taxonomic_category(self, category_id: int, kingdom: str, phylum: str, t_class: str, t_order: str, family: str, genus: str):
        with self.db.get_session() as session:
            category = session.get(TaxonomicCategory, category_id)
            if category:
                category.kingdom = kingdom
                category.phylum = phylum
                category.t_class = t_class
                category.t_order = t_order
                category.family = family
                category.genus = genus
                session.commit()
                session.refresh(category)
                return category
            return None

    def delete_taxonomic_category(self, category_id: int):
        with self.db.get_session() as session:
            category = session.get(TaxonomicCategory, category_id)
            if category:
                session.delete(category)
                session.commit()
                return True
            return False
