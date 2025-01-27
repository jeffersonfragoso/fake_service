from typing import List
from sqlmodel import Field, SQLModel, Relationship, select


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)
    username: str
    role: str = Field(index=True)
    encrypted_password: str


class ReportModel(SQLModel, table=True):
    __tablename__ = "report"

    id: int = Field(primary_key=True)
    title: str
    status: str
    admin_report_id: int = Field(foreign_key="admin_report.id")
    admin_report: "AdminReportModel" = Relationship(back_populates="reports")


class AdminReportModel(SQLModel, table=True):
    __tablename__ = "admin_report"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    reports: List[ReportModel] = Relationship(back_populates="admin_report")


class PurchaseModel(SQLModel, table=True):
    __tablename__ = "purchase"

    id: int = Field(primary_key=True)
    item: str
    price: float
    user_purhchase_id: int = Field(foreign_key="user_purhchase.id")
    user_purhchase: "UserPurchaseModel" = Relationship(back_populates="purchases")


class UserPurchaseModel(SQLModel, table=True):
    __tablename__ = "user_purhchase"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    purchases: List[PurchaseModel] = Relationship(back_populates="user_purhchase")
