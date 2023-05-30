from django.urls import path
from .import views

urlpatterns = [
    path("", views.product, name="product"),
    path("cart/", views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name= "add"),
    path("delete_cart", views.delete_cart, name="delete")
    # path("confirm_payment/<str:pk>", views.confirm_payment, name="add"),
]