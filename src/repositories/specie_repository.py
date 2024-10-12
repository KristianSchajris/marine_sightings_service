# src/repositories/specie_repository.py

from src.models.specie import Specie
from src.connect.db_connect import DatabaseConnet
from src.repositories.base.base_repository import BaseRepository

class SpecieRepository(BaseRepository):
    def __init__(self):
        super().__init__(DatabaseConnet())

    def create(self, common_name: str, scientific_name: str):
        new_specie = Specie(common_name=common_name, scientific_name=scientific_name)
        return super().create(new_specie)

    def get(self, specie_id: int):
        return super().get(Specie, specie_id)

    def get_all(self):
        return super().get_all(Specie)

    def update(self, specie_id: int, common_name: str, scientific_name: str):
        specie = self.get(specie_id)
        if specie:
            return super().update(specie, common_name=common_name, scientific_name=scientific_name)
        return None

    def delete(self, specie_id: int):
        specie = self.get(specie_id)
        if specie:
            return super().delete(specie)
        return False
