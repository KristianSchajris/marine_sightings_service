# src/services/specie_service.py
from src.models.specie import Specie
from src.repositories.specie_repository import SpecieRepository

class SpecieService:
    def __init__(self):
        self.repository = SpecieRepository()
    
    def create_specie(self, common_name: str, scientific_name: str) -> Specie:
        return self.repository.create(common_name=common_name, scientific_name=scientific_name)

    def get_specie(self, specie_id: int) -> Specie:
        return self.repository.get(specie_id)

    def get_all_species(self) -> list[Specie]:
        return self.repository.get_all()

    def update_specie(self, specie_id: int, common_name: str, scientific_name: str) -> Specie:
        return self.repository.update(specie_id, common_name=common_name, scientific_name=scientific_name)

    def delete_specie(self, specie_id: int) -> bool:
        return self.repository.delete(specie_id)
