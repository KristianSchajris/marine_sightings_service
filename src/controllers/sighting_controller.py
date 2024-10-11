from sqlmodel import Session
from src.models.sighting import Sighting
from src.connect.db_connect import Database

class SightingController:
    def __init__(self):
        self.db = Database()

    def create_sighting(self, latitude: float, longitude: float, image_sighting: str, notes: str, place_id: int, specie_id: int, user_id: int):
        with self.db.get_session() as session:
            new_sighting = Sighting(latitude=latitude, longitude=longitude, image_sighting=image_sighting, notes=notes, place_id=place_id, specie_id=specie_id, user_id=user_id)
            session.add(new_sighting)
            session.commit()
            session.refresh(new_sighting)
            return new_sighting

    def get_sighting(self, sighting_id: int):
        with self.db.get_session() as session:
            return session.get(Sighting, sighting_id)
    
    def get_all_sightings(self):
        with self.db.get_session() as session:
            return session.query(Sighting).all()

    def update_sighting(self, sighting_id: int, latitude: float, longitude: float, image_sighting: str, notes: str):
        with self.db.get_session() as session:
            sighting = session.get(Sighting, sighting_id)
            if sighting:
                sighting.latitude = latitude
                sighting.longitude = longitude
                sighting.image_sighting = image_sighting
                sighting.notes = notes
                session.commit()
                session.refresh(sighting)
                return sighting
            return None

    def delete_sighting(self, sighting_id: int):
        with self.db.get_session() as session:
            sighting = session.get(Sighting, sighting_id)
            if sighting:
                session.delete(sighting)
                session.commit()
                return True
            return False
