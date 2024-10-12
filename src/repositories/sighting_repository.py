# src/repositories/sighting_repository.py

from sqlmodel import Session
from src.models.sighting import Sighting
from src.connect.db_connect import DatabaseConnet
from src.repositories.base.base_repository import BaseRepository

class SightingRepository(BaseRepository):
    def __init__(self):
        super().__init__(DatabaseConnet())
    
    def create(self, latitude: float, longitude: float, image_sighting: str, notes: str, place_id: int, specie_id: int, user_id: int):
        new_sighting = Sighting(latitude=latitude, longitude=longitude, image_sighting=image_sighting, notes=notes, place_id=place_id, specie_id=specie_id, user_id=user_id)
        return super().create(new_sighting)
    
    def get(self, sighting_id: int):
        return super().get(Sighting, sighting_id)
    
    def get_all(self):
        return super().get_all(Sighting)
    
    def get_sightings_by_user(self, user_id: int) -> list[Sighting]:
        return super().get_all(Sighting, user_id=user_id)
    
    def update(self, sighting_id: int, latitude: float, longitude: float, image_sighting: str, notes: str, place_id: int, specie_id: int, user_id: int):
        sighting = self.get(sighting_id)
        if sighting:
            return super().update(sighting, latitude=latitude, longitude=longitude, image_sighting=image_sighting, notes=notes, place_id=place_id, specie_id=specie_id, user_id=user_id)
        return None
    
    def delete(self, sighting_id: int):
        sighting = self.get(sighting_id)
        if sighting:
            return super().delete(sighting)
        return False
