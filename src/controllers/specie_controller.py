from src.models.specie import Specie
from src.services.specie_service import SpecieService

class SpecieController:
    def __init__(self):
        self.service = SpecieService()

    def create_specie(self, common_name: str, scientific_name: str) -> Specie:
        return self.service.create_specie(common_name=common_name, scientific_name=scientific_name)

    def get_specie(self, specie_id: int) -> Specie:
        return self.service.get_specie(specie_id)

    def get_all_species(self) -> list[Specie]:
        return self.service.get_all_species()

    def update_specie(self, specie_id: int, common_name: str, scientific_name: str) -> Specie:
        return self.service.update_specie(specie_id, common_name=common_name, scientific_name=scientific_name)

    def delete_specie(self, specie_id: int) -> bool:
        return self.service.delete_specie(specie_id)
