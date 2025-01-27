from sqlmodel import SQLModel, create_engine, Session, select

from src.core._shared.infraestructure.crypt import Crypt
from src.core._shared.infraestructure.orm import User

engine = create_engine("sqlite:///database.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def seed_database():
    admin = User(
        username="admin",
        role="admin",
        encrypted_password=Crypt.encrypt_secret("JKSipm0YH")
    )
    user = User(
        username="user",
        role="user",
        encrypted_password=Crypt.encrypt_secret("L0XuwPOdS5U")
    )

    with Session(engine) as session:
        session.add(admin)
        session.add(user)
        session.commit()

def factory_session() -> Session:
    return Session(engine)
