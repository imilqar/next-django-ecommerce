from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="store_products"),
    path("category/", views.CategoryListView.as_view(), name="categories"),
    path("products/<slug:slug>/", views.ProductView.as_view(), name="product"),
    path(
        "category/<slug:slug>/",
        views.CategoryItemView.as_view(),
        name="category_item",
    ),
]
