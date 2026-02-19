from django.urls import path

from .http.views import LandUseAreaView, LandUseOptionsView, PlacePointView

urlpatterns = [
    path("places/points/", PlacePointView.as_view(), name="place-points"),
    path("places/land-uses/", LandUseOptionsView.as_view(), name="place-land-use-options"),
    path("places/land-uses/area/", LandUseAreaView.as_view(), name="place-land-use-area"),
]
