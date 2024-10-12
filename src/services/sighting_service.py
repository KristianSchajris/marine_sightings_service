# src/services/sighting_service.py
from src.adapters.xml_response_adapter import XMLAdapter
from src.repositories.sighting_repository import SightingRepository
from src.models.sighting import Sighting
from src.utilities.logger.logger import log_method_call
from src.utilities.pagination.paginated_collection import PaginatedCollection

class SightingService:
    def __init__(self):
        self.repository = SightingRepository()
    
    @log_method_call
    def create_sighting(self, latitude: float, longitude: float, image_sighting: str, notes: str, place_id: int, specie_id: int, user_id: int) -> Sighting:
        return self.repository.create(
            latitude=latitude, 
            longitude=longitude, 
            image_sighting=image_sighting, 
            notes=notes, 
            place_id=place_id, 
            specie_id=specie_id, 
            user_id=user_id
        )
    
    @log_method_call
    def get_sighting(self, sighting_id: int) -> Sighting:
        return self.repository.get(sighting_id)
    
    def get_sighting_xml(self, sighting_id: int) -> str:
        sighting = self.get_sighting(sighting_id)
        return XMLAdapter(sighting).to_xml()
    
    @log_method_call
    def get_all_sightings(self) -> list[Sighting]:
        return self.repository.get_all()
    
    @log_method_call
    def get_sightings_by_user(self, user_id: int) -> list[Sighting]:
        return self.repository.get_sightings_by_user(user_id)
    
    @log_method_call
    def update_sighting(self, sighting_id: int, latitude: float, longitude: float, image_sighting: str, notes: str) -> Sighting:
        return self.repository.update(
            sighting_id, 
            latitude=latitude, 
            longitude=longitude, 
            image_sighting=image_sighting, 
            notes=notes
        )
    
    @log_method_call
    def delete_sighting(self, sighting_id: int) -> bool:
        return self.repository.delete(sighting_id)

    @log_method_call
    def get_paginated_sightings(self, page: int, page_size: int) -> PaginatedCollection:
        sightings = self.repository.get_all()  # Obtener todos los avistamientos
        return PaginatedCollection(sightings, page, page_size)  # Devolver una colección paginada
