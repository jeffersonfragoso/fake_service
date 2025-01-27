from sqlmodel import SQLModel, create_engine, Session, select

from src.core._shared.infraestructure.crypt import Crypt
from src.core._shared.infraestructure.orm import UserModel
from src.core._shared.config import get_settings

variables = get_settings()

engine = create_engine(variables.DB_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def seed_database():
    admin = UserModel(
        username=variables.DEFAULT_ADMIN,
        role="admin",
        encrypted_password=Crypt.encrypt_secret(variables.DEFAULT_ADMIN_PASSWORD)
    )
    user = UserModel(
        username=variables.DEFAULT_USER,
        role="user",
        encrypted_password=Crypt.encrypt_secret(variables.DEFAULT_USER_PASSWORD)
    )

    with Session(engine) as session:
        session.add(admin)
        session.add(user)
        session.commit()

def factory_session() -> Session:
    return Session(engine)
