from django.shortcuts import render
from .models import Product, Cart
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@login_required(login_url='login')
def cart_detail(request):
    cart = Cart.objects.first()  # Assuming there's only one cart for simplicity
    return render(request, 'cart.html', {'cart': cart})
