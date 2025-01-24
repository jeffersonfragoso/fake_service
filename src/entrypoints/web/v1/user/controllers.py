from fastapi import APIRouter

from src.entrypoints.web.v1.user.schemas import UserResponse, User, Purchases

user_router = APIRouter()


@user_router.get("/", response_model=UserResponse)
async def get():
    return UserResponse(
        message="Hello, user!",
        data=User(
            name="John Doe",
            email="john@example.com",
            purchases=[
                Purchases(id=1, item="Laptop", price=2500),
                Purchases(id=2, item="Smartphone", price=1200),
            ]
        )
    )
