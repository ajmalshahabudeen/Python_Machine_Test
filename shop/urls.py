from django.urls import path
from .import views

urlpatterns = [
    path("", views.product, name="product"),
    path("cart/", views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name= "add"),
    path("update_cart/<int:id>/", views.update_cart, name="update_cart"),
    path("delete_cart/<int:id>/", views.delete_cart, name="delete_cart"),
    # path("confirm_payment/<str:pk>", views.confirm_payment, name="add"),
]