from django.contrib.auth.hashers import check_password

from ...infrastructure.repositories.user_repository import UserRepository
from ...domain.exceptions.invalid_credentials import InvalidCredentialsException


class LoginUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, username: str, password: str):
        user = self.repository.get_by_username(username)

        if not user:
            raise InvalidCredentialsException()

        if not check_password(password, user.password):
            raise InvalidCredentialsException()

        return user
