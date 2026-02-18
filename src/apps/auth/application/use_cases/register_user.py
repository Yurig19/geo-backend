from ...infrastructure.repositories.user_repository import UserRepository
from ...domain.exceptions.user_exists import UserAlreadyExistsException


class RegisterUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, username: str, email: str, password: str):
        user_exists = self.repository.get_by_username(username)

        if user_exists:
            raise UserAlreadyExistsException()

        user = self.repository.create(username, email, password)

        return user
