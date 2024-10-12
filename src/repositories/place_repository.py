# src/repositories/place_repository.py

from sqlmodel import Session
from src.models.place import Place
from src.connect.db_connect import DatabaseConnet
from src.repositories.base.base_repository import BaseRepository

class PlaceRepository(BaseRepository):
    def __init__(self):
        super().__init__(DatabaseConnet())
    
    def create(self, name_place: str, country: str, state: str):
        new_place = Place(name_place=name_place, country=country, state=state)
        return super().create(new_place)
    
    def get(self, place_id: int):
        return super().get(Place, place_id)
    
    def get_all(self):
        return super().get_all(Place)
    
    def get_place_by_country(self, country: str):
        return super().get_all(Place, country=country)
    
    def get_place_by_state(self, state: str):
        return super().get_all(Place, state=state)
    
    
    def update(self, place_id: int, name_place: str, country: str, state: str):
        place = self.get(place_id)
        if place:
            return super().update(place, name_place=name_place, country=country, state=state)
        return None 
    
    def delete(self, place_id: int):
        place = self.get(place_id)
        if place:
            return super().delete(place)
        return False
