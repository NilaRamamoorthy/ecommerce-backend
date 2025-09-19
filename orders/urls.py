from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, CheckoutView, OrderListView

urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/add/", AddToCartView.as_view(), name="cart-add"),
    path("cart/remove/", RemoveFromCartView.as_view(), name="cart-remove"),
    path("", OrderListView.as_view(), name="orders"),  # <-- no "orders/"
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
