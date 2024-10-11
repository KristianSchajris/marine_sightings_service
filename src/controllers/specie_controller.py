from sqlmodel import Session
from src.models.specie import Specie
from src.connect.db_connect import Database

class SpecieController:
    def __init__(self):
        self.db = Database()

    def create_specie(self, common_name: str, scientific_name: str):
        with self.db.get_session() as session:
            new_specie = Specie(common_name=common_name, scientific_name=scientific_name)
            session.add(new_specie)
            session.commit()
            session.refresh(new_specie)
            return new_specie

    def get_specie(self, specie_id: int):
        with self.db.get_session() as session:
            return session.get(Specie, specie_id)
    
    def get_all_species(self):
        with self.db.get_session() as session:
            return session.query(Specie).all()

    def update_specie(self, specie_id: int, common_name: str, scientific_name: str):
        with self.db.get_session() as session:
            specie = session.get(Specie, specie_id)
            if specie:
                specie.common_name = common_name
                specie.scientific_name = scientific_name
                session.commit()
                session.refresh(specie)
                return specie
            return None

    def delete_specie(self, specie_id: int):
        with self.db.get_session() as session:
            specie = session.get(Specie, specie_id)
            if specie:
                session.delete(specie)
                session.commit()
                return True
            return False
