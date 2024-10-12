from sqlmodel import Session

from src.interface.base_repository_interface import BaseRepositoryInterface

class BaseRepository(BaseRepositoryInterface):
    def __init__(self, db_connection):
        self.db = db_connection

    def create(self, model):
        with self.db.get_session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    def get(self, model_class, model_id: int):
        with self.db.get_session() as session:
            return session.get(model_class, model_id)

    def get_all(self, model_class):
        with self.db.get_session() as session:
            return session.query(model_class).all()

    def update(self, model_instance, **kwargs):
        with self.db.get_session() as session:
            if not session.is_modified(model_instance):
                session.add(model_instance)
            for key, value in kwargs.items():
                setattr(model_instance, key, value)
            session.commit()
            session.refresh(model_instance)
            return model_instance

    def delete(self, model_instance):
        with self.db.get_session() as session:
            session.delete(model_instance)
            session.commit()
            return True
