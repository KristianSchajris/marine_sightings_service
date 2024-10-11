from sqlmodel import Session

from src.connect.db_connect import Database
from src.models.place import Place

class PlaceController:
    def __init__(self):
        self.db = Database()

    def create_place(self, name_place: str, country: str, state: str):
        with self.db.get_session() as session:
            new_place = Place(name_place=name_place, country=country, state=state)
            session.add(new_place)
            session.commit()
            session.refresh(new_place)
            return new_place

    def get_place(self, place_id: int):
        with self.db.get_session() as session:
            return session.get(Place, place_id)
    
    def get_all_places(self):
        with self.db.get_session() as session:
            return session.query(Place).all()

    def update_place(self, place_id: int, name_place: str, country: str, state: str):
        with self.db.get_session() as session:
            place = session.get(Place, place_id)
            if place:
                place.name_place = name_place
                place.country = country
                place.state = state
                session.commit()
                session.refresh(place)
                return place
            return None

    def delete_place(self, place_id: int):
        with self.db.get_session() as session:
            place = session.get(Place, place_id)
            if place:
                session.delete(place)
                session.commit()
                return True
            return False
