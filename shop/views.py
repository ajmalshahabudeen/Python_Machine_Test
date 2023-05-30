from django.shortcuts import render
from .models import Product, Cart

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def cart_detail(request):
    cart = Cart.objects.first()  # Assuming there's only one cart for simplicity
    return render(request, 'cart.html', {'cart': cart})
