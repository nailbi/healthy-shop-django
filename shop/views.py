from django.shortcuts import render, redirect
from .models import Product
from orders.models import Favorite
from django.db.models import Q


def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    recommended = Product.objects.order_by('-rating')[:4]

    return render(request, 'shop/products.html', {
        'products': products,
        'recommended': recommended
    })

