from django.urls import path

from .http.views import PlaceCreateView

urlpatterns = [
    path("places/", PlaceCreateView.as_view(), name="create-place"),
]
