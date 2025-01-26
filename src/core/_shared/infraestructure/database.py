from sqlmodel import SQLModel, create_engine, Session, select

engine = create_engine("sqlite:///database.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def factory_session() -> Session:
    return Session(engine)
