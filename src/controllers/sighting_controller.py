from src.models.sighting import Sighting
from src.services.sighting_service import SightingService
from src.utilities.pagination.paginated_collection import PaginatedCollection

class SightingController:
    def __init__(self):
        self.service = SightingService()

    def create_sighting(self, latitude: float, longitude: float, image_sighting: str, notes: str, place_id: int, specie_id: int, user_id: int) -> Sighting:
        return self.service.create_sighting(latitude=latitude, longitude=longitude, image_sighting=image_sighting, notes=notes, place_id=place_id, specie_id=specie_id, user_id=user_id)

    def get_sighting(self, sighting_id: int) -> Sighting:
        return self.service.get_sighting(sighting_id)
    
    def get_sighting_xml(self, sighting_id: int) -> str:
        return self.service.get_sighting_xml(sighting_id)

    def get_all_sightings(self) -> list[Sighting]:
        return self.service.get_all_sightings()

    def update_sighting(self, sighting_id: int, latitude: float, longitude: float, image_sighting: str, notes: str) -> Sighting:
        return self.service.update_sighting(sighting_id, latitude=latitude, longitude=longitude, image_sighting=image_sighting, notes=notes)

    def delete_sighting(self, sighting_id: int) -> bool:
        return self.service.delete_sighting(sighting_id)

    def get_paginated_sightings(self, page: int, page_size: int) -> PaginatedCollection:
        return self.service.get_paginated_sightings(page, page_size)
