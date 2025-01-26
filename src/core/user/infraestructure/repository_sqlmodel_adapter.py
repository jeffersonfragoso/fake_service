from typing import List
from sqlmodel import Field, SQLModel, Relationship



class ReportModel(SQLModel, table=True):
    __tablename__ = "report"

    id: int = Field(primary_key=True)
    title: str
    status: str
    user_id: int = Field(foreign_key="user.id")
    user: "UserModel" = Relationship(back_populates="reports")


class PurchaseModel(SQLModel, table=True):
    __tablename__ = "purchase"

    id: int = Field(primary_key=True)
    item: str
    price: float
    user_id: int = Field(foreign_key="user.id")
    user: "UserModel" = Relationship(back_populates="purchases")


class UserModel(SQLModel, table=True):
    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    hashed_password: str
    purchases: List[PurchaseModel] | None = Relationship(back_populates="user")
    reports: List[ReportModel] | None = Relationship(back_populates="user")
