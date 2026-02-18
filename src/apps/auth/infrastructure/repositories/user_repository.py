from typing import Optional
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

User = get_user_model()


class UserRepository:

    def create(
        self,
        username: str,
        email: str,
        password: str,
    ) -> AbstractBaseUser:
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

    def get_by_username(
        self,
        username: str,
    ) -> Optional[AbstractBaseUser]:
        return User.objects.filter(username=username).first()
