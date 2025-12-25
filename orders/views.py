from django.shortcuts import redirect, render
from .models import CartItem


def add_to_cart(request, product_id):
    CartItem.objects.create(user=request.user, product_id=product_id)
    return redirect('/')


def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'orders/cart.html', {'items': items})

from django.shortcuts import render, redirect
from .models import Favorite

def favorites_view(request):
    items = Favorite.objects.filter(user=request.user)
    return render(request, 'orders/favorites.html', {'items': items})
