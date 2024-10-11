from sqlmodel import SQLModel, create_engine, Session

class Database:
    def __init__(self):
        self.engine = create_engine(
            "sqlite:///marine_sightings.db",
            connect_args={"check_same_thread": False}
        )
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        return Session(self.engine)
