# src/services/place_service.py
from src.adapters.xml_response_adapter import XMLAdapter
from src.repositories.place_repository import PlaceRepository
from src.models.place import Place
from src.utilities.logger.logger import log_method_call
from src.utilities.pagination.paginated_collection import PaginatedCollection

class PlaceService:
    def __init__(self):
        self.repository = PlaceRepository()

    @log_method_call
    def create_place(self, name_place: str, country: str, state: str) -> Place:
        return self.repository.create(name_place=name_place, country=country, state=state)

    @log_method_call
    def get_place(self, place_id: int) -> Place:
        return self.repository.get(place_id)

    @log_method_call
    def get_all_places(self) -> list[Place]:
        return self.repository.get_all()
    
    @log_method_call
    def get_place_by_country(self, country: str) -> list[Place]:
        return self.repository.get_place_by_country(country)
    
    @log_method_call
    def get_place_xml(self, place_id: int) -> str:
        place = self.get_place(place_id)
        return XMLAdapter(place).to_xml()
    
    @log_method_call
    def get_all_with_pagination(self, page: int, page_size: int) -> list[Place]:
        #places = self.repository.get_all()
        #start_index = (page - 1) * page_size
        #end_index = start_index + page_size
        #return places[start_index:end_index]

        places = self.repository.get_all()
        return PaginatedCollection(places, page, page_size)

    @log_method_call
    def get_place_by_state(self, state: str) -> list[Place]:
        return self.repository.get_place_by_state(state)

    @log_method_call
    def update_place(self, place_id: int, name_place: str, country: str, state: str) -> Place:
        return self.repository.update(place_id, name_place=name_place, country=country, state=state)

    @log_method_call
    def delete_place(self, place_id: int) -> bool:
        return self.repository.delete(place_id)
