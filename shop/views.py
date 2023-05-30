import json
from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def product(request):
    products = Product.objects.all()
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        
    context = {"products":products, "cart": cart}
    return render(request, "products.html", context)

@login_required(login_url='login')
def cart(request):
    
    cart = None
    cartitems = []
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
    
    context = {"cart":cart, "items":cartitems}
    return render(request, "cart.html", context)

@login_required(login_url='login')
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        
        
        num_of_item = cart.num_of_items
        
        print(cartitem)
    return JsonResponse(num_of_item, safe=False)

@login_required(login_url='login')
def delete_cart(request):
    if request.method == 'POST':
        # Delete the cart for the logged-in user
        cart = Cart.objects.get(user=request.user)
        cart.delete()
        return redirect('cart')  # Redirect to the cart page or any other desired page
    else:
        return redirect('cart')  # Redirect to the cart page or any other desired page
