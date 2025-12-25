from django.urls import path
from .views import cart_view, add_to_cart

urlpatterns = [
    path('cart/', cart_view),
    path('add-to-cart/<int:product_id>/', add_to_cart),
]

from django.urls import path
from .views import cart_view, add_to_cart, favorites_view

urlpatterns = [
    path('cart/', cart_view),
    path('add-to-cart/<int:product_id>/', add_to_cart),

    # ✅ ВАЖНО — ИЗБРАННОЕ
    path('favorites/', favorites_view),
]
