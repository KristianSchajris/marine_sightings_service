from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.ext.declarative import declarative_base

class DatabaseConnet:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DatabaseConnet, cls).__new__(cls)
            cls.__instance.engine = create_engine(
                "sqlite:///marine_sightings.db", 
                connect_args={"check_same_thread": False}
            )
            SQLModel.metadata.create_all(cls.__instance.engine)
        return cls.__instance

    def get_session(self):
        return Session(self.__instance.engine)
