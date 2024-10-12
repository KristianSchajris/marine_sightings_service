from src.models.place import Place
from src.services.place_service import PlaceService

class PlaceController:
    def __init__(self):
        self.service = PlaceService()

    def create_place(self, name_place: str, country: str, state: str) -> Place:
        return self.service.create_place(name_place=name_place, country=country, state=state)

    def get_place(self, place_id: int) -> Place:
        return self.service.get_place(place_id)
    
    def get_all(self) -> list[Place]:
        return self.service.get_all_places()

    def get_all_places(self) -> list[Place]:
        return self.service.get_all_places()
    
    def get_all_with_pagination(self, page: int, page_size: int) -> list[Place]:
        return self.service.get_all_with_pagination(page, page_size)

    def update_place(self, place_id: int, name_place: str, country: str, state: str) -> Place:
        return self.service.update_place(place_id, name_place=name_place, country=country, state=state)

    def delete_place(self, place_id: int) -> bool:
        return self.service.delete_place(place_id)
