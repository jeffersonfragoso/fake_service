from src.core.user.infraestructure.repository_interface import AbstractRepository
from src.core.user.application.use_cases.dto import UserDto
from src.core.user.infraestructure.repository_sqlmodel_adapter import UserModel
from src.core._shared.infraestructure.database import engine, Session, select


class GetUser():

    def execute(self) -> UserDto.OutPutGetUser:
        try:
            with Session(engine) as session:
                statement = select(UserModel)
                user_db = session.exec(statement).first()

                purchases = [UserDto.PurchaseDto(**item.model_dump()) for item in user_db.purchases]

                output = UserDto.OutPutGetUser(
                    **user_db.model_dump(),
                    purchases=purchases
                )

                return output
        except Exception as e:
            pass
