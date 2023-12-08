from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'pharmacie/index.html',{'name':'oussama','age':25})

def home(request):
    return render(request,'pharmacie/home.html')

def shop(request):
    return render(request,'pharmacie/shop.html')

def about(request):
    return render(request,'pharmacie/about.html')

def contact(request):
    return render(request,'pharmacie/contact.html')

def cart(request):
    return render(request,'pharmacie/cart.html')

def shop_single(request):
    return render(request,'pharmacie/shop-single.html')

def checkout(request):
    return render(request,'pharmacie/checkout.html')

def thankyou(request):
    return render(request,'pharmacie/thankyou.html')

def ByBy(request):
    return render(request,'pharmacie/ByBy.html')

