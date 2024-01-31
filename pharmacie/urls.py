from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("home", views.home, name="home"),
    path("shop/home", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("shop/shop", views.shop, name="shop"),
    path("about", views.about, name="about"),
    path("shop/about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("shop/contact", views.contact, name="contact"),
    path("cart", views.cart3, name="cart"),
    path("shop/cart", views.cart3, name="cart"),
    path("shop/shop_single", views.shop_single, name="shop_single"),
    path("shop_single", views.shop_single, name="shop_single"),
    path("checkout", views.checkout, name="checkout"),
    path("shop/checkout", views.checkout, name="checkout"),
    path("thankyou", views.thankyou, name="thankyou"),
    path("shop/thankyou", views.thankyou, name="thankyou"),
    path("thankyouMessage", views.thankyouMessage, name="thankyouMessage"),
    path("byBy", views.ByBy, name="byBy"),
    path("supprimerP", views.supprimerP, name="supprimerP"),
    path("Ab", views.about2, name="about2"),
    path("session1", views.sessionCreate, name="session1"),
]
