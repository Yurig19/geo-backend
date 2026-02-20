from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .http.views.register_view import RegisterView
from .http.views.login_view import LoginView
from .http.views.token_validation_view import TokenValidationView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("check-token/", TokenValidationView.as_view(), name="check_token"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
