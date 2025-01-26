from src.core.user.application.use_cases.dto import UserDto
from src.core.user.infraestructure.repository_sqlmodel_adapter import UserModel, PurchaseModel
from src.core._shared.infraestructure.database import engine, Session


class CreateUser():

    def execute(self, input_create: UserDto.InputNewUser) -> None:
        try:

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

        except Exception as e:
            pass
