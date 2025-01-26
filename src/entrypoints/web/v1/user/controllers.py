from fastapi import APIRouter, Depends

from src.core._shared.infraestructure.fastapi_auth_adapter import FastApiAuthAdapter
from src.entrypoints.web.v1.user.schemas import InputCreateUser, UserResponse, UserSchema, PurchaseSchema
from src.core.user.infraestructure.repository_sqlmodel_adapter import PurchaseModel, UserModel
from src.core._shared.infraestructure.database import engine, Session, select

user_router = APIRouter()


@user_router.get(
    "/",
    response_model=UserResponse,
    dependencies=[Depends(FastApiAuthAdapter.has_role(role="user"))]
)
async def get():
    with Session(engine) as session:
        statement = select(UserModel)
        user_db = session.exec(statement).first()

        purchases = [PurchaseSchema(**item.model_dump()) for item in user_db.purchases]

        return UserResponse(
            message="Hello, user!",
            data=UserSchema(
                name=user_db.name,
                email=user_db.email,
                purchases=purchases
            )
        )

@user_router.post("/")
async def post(input_create: InputCreateUser):
    purchases = [PurchaseModel(**item.model_dump()) for item in input_create.purchases]
    new_user = UserModel(
        name=input_create.name,
        email=input_create.email,
        hashed_password=input_create.password,
        purchases=purchases
    )

    with Session(engine) as session:
        session.add(new_user)
        session.commit()
