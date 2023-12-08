from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("shop", views.shop, name="shop"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("cart", views.cart, name="cart"),
    path("shop_single", views.shop_single, name="shop_single"),
    path("checkout", views.checkout, name="checkout"),
    path("thankyou", views.thankyou, name="thankyou"),
    path("byBy", views.ByBy, name="byBy"),
]
