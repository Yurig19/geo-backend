from django.urls import path

from .http.views.products_view import (
    ProductAddStockView,
    ProductCreateView,
    ProductDetailView,
    ProductRemoveStockView,
)

urlpatterns = [
    path("products/", ProductCreateView.as_view(), name="create-product"),
    path("products/<uuid:product_id>/", ProductDetailView.as_view(), name="product-detail"),
    path(
        "products/<uuid:product_id>/stock/add/",
        ProductAddStockView.as_view(),
        name="product-add-stock",
    ),
    path(
        "products/<uuid:product_id>/stock/remove/",
        ProductRemoveStockView.as_view(),
        name="product-remove-stock",
    ),
]
