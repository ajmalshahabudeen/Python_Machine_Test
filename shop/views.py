import json
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Cart, CartItem
from django.http import JsonResponse, HttpResponseRedirect
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
def delete_cart(request, id):
    if request.method == 'POST':
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
            print("worked")
        except Cart.DoesNotExist:
            print("failed")
            return HttpResponseRedirect(reverse("cart"))
        
        try:
            cartitem = CartItem.objects.get(id=id)
            cartitem.cart = None
            cartitem.save()
            return HttpResponseRedirect(reverse("cart"))
        except CartItem.DoesNotExist:
            # Handle case when the CartItem with the given ID does not exist
            pass
    
    # Redirect to the cart page if the request is not a POST request
    return HttpResponseRedirect(reverse("cart"))
    
    # try:
    #     the_id = request.session['product_id']
    #     cart = Cart.objects.get(id=the_id)
    #     print("worked")
    # except:
    #     print("failed")
    #     return HttpResponseRedirect(reverse("cart"))
    
    # cartitem = CartItem.objects.get(id=id)
    # # cartitem.delete()
    # cartitem.cart = None
    # cartitem.save()
    # return HttpResponseRedirect(reverse("cart"))