from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    return render(request, 'products/product.html',context={'pro':Product.objects.get(id=1)})

def products(request):
    pro = Product.objects.all()
    #x = context = {'pro': pro.filter(category='phone')}
    return render(request, 'products/products.html',context={'pro':pro})