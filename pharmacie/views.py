import requests
from django.shortcuts import render, get_object_or_404
from django.template import context

from .models import Login,Contact,Client
from products.models import Product


# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'pharmacie/index.html', {'name': 'oussama', 'age': 25})


def home(request):
    x = Product.objects.all()
    y = Product.objects.all().filter(new=True)
    return render(request, 'pharmacie/home.html', context={'x': x, 'y': y})


def shop(request):
    order_by = request.GET.get('order_by', '')

    if order_by:
        # La valeur de order_by n'est pas vide, vous pouvez la traiter
        if order_by == 'name_asc':
            products = Product.objects.all().order_by('name')
        elif order_by == 'name_desc':
            products = Product.objects.all().order_by('-name')
        elif order_by == 'price_asc':
            products = Product.objects.all().order_by('price')
        elif order_by == 'price_desc':
            products = Product.objects.all().order_by('-price')
        else:
            # Valeur order_by non reconnue, gérer selon vos besoins
            products = Product.objects.all()
    else:
        # Aucune valeur de order_by, traitement par défaut
        products = Product.objects.all()

    context = {'products': products}
    return render(request, 'pharmacie/shop.html', context)

def about(request):
    return render(request, 'pharmacie/about.html')


def contact(request):
    fn = request.POST.get('fn')
    ln = request.POST.get('ln')
    gml = request.POST.get('eml')
    sub = request.POST.get('sub')
    msg = request.POST.get('msg')

    if ln and gml and sub and msg:
        data = Contact(fn=fn, ln=ln, eml=gml, sub=sub, msg=msg)
        data.save()
        return render(request, 'pharmacie/thankyouMessage.html')

    return render(request, 'pharmacie/contact.html')


"""def cart(request):
    name_p = request.GET.get('name')
    nbr = request.GET.get('nbr')
    product = Product.objects.get(name=name_p)
    recently_viewed_products =  None


    if 'recently_viewed' in request.session:
        if product.id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product.id)

        recently_viewed_products =Product.objects.filter(pk__in=request.session['recently_viewed'])
        request.session['recently_viewed'].insert(0, product.id)

    else:
        request.session['recently_viewed'] = [product.id]

    request.session.modified = True
    context = {'product': product, 'recently_viewed_products': recently_viewed_products}
    return render(request, 'pharmacie/cart.html', context)"""


def cart2(request):
        id = request.GET.get('id')

        product = Product.objects.get(id=id)
        print("Salaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaam    id = "+id)

        recently_viewed_products = None


        if 'recently_viewed' in request.session :
             if id in request.session['recently_viewed']:
                 request.session['recently_viewed'].remove(id)
                 recently_viewed_products = Product.objects.filter(id__in=request.session['recently_viewed'])
                 request.session['recently_viewed'].insert(0, id)
                 print("Cococcccccccccccccccccccc")
        else:
            request.session['recently_viewed'] = [id]
            recently_viewed_products = Product.objects.filter(id__in=request.session['recently_viewed'])
            print("Wooooooooooooooooooooooooooooooo")

        ### Update pardefault of the session
        request.session.modified = True

        context = {'product':product,'recently_viewed_products':recently_viewed_products}
        return render(request, 'pharmacie/cart.html', context)

def cart3(request):
    id = request.GET.get('id')
    product = get_object_or_404(Product, id=id)
    print(f"Salaaaaam id = {id}")

    recently_viewed_products = None
    recently_viewed = request.session.get('recently_viewed', [])

    if id in recently_viewed:
        recently_viewed.remove(id)
        recently_viewed.insert(0, id)
        print("Cococcccccccccccccccccccc")
    else:
        recently_viewed = [id]
        print("Wooooooooooooooooooooooooooooooo")

    request.session['recently_viewed'] = recently_viewed
    request.session.modified = True

    recently_viewed_products = Product.objects.filter(id__in=recently_viewed)
    total = 0
    for p in recently_viewed_products:
        total += p.price

    context = {'product': product, 'recently_viewed_products': recently_viewed_products, 'total':total}
    return render(request, 'pharmacie/cart.html', context)




from django.shortcuts import get_object_or_404

def supprimerP(request):
    if request.GET.get('id'):
        id = request.GET.get('id')
        p = get_object_or_404(Product, id=id)

        if 'recently_viewed' in request.session:
            recently_viewed = request.session['recently_viewed']

            # Vérifier si le produit est déjà dans la liste
            for item in recently_viewed:
                if isinstance(item, dict) and item.get('id') == id:
                    recently_viewed.remove(item)
                    break

    return render(request, 'pharmacie/cart.html')


def shop_single(request):
    n = request.GET.get('name')
    x = Product.objects.get(name=n)
    return render(request, 'pharmacie/shop-single.html',context={'name':x})


def checkout(request):
    if request.method == 'POST':       #done
        print("Salaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaam")
        fn = request.POST.get('fn')     #done
        ln = request.POST.get('ln')     #done
        eml = request.POST.get('eml')   #done
        adr = request.POST.get('addr')   #done
        cont = request.POST.get('cont')   #done
        post = request.POST.get('postt')  #done
        pho = request.POST.get('phon')    #done
        pas = request.POST.get('pas')     #done


        if fn and ln and eml and adr and cont and post and pho and pas:
            data = Client(fn=fn, ln=ln, eml=eml, adr=adr, cont=cont, post=post, pho=pho, pas=pas)
            data.save()
            return render(request, 'pharmacie/thankyou.html')



    return render(request, 'pharmacie/checkout.html')


def thankyou(request):
    return render(request, 'pharmacie/thankyou.html')


from django.shortcuts import render
from .models import Client


def ByBy(request):
    remis = request.GET.get("remis")

    # Utilisez try-except pour gérer le cas où aucun client n'est trouvé avec le code_remis donné
    try:
        client = Client.objects.get(code_remis=remis)
    except Client.DoesNotExist:
        return render(request, 'pharmacie/checkout.html')

    # Si le client est trouvé, effectuez les modifications et enregistrez
    percentage_remis = client.percentage_remis + 0.1
    fn = client.fn
    ln = client.ln
    eml = client.eml
    adr = client.adr
    cont = client.cont
    post = client.post
    pho = client.pho
    pas = client.pas
    code_remis = client.code_remis

    # Créez un nouvel objet Client avec les modifications
    updated_client = Client(
        fn=fn, ln=ln, eml=eml, adr=adr, cont=cont, post=post, pho=pho, pas=pas,
        percentage_remis=percentage_remis, code_remis=code_remis
    )

    # Enregistrez le nouvel objet Client
    updated_client.save()

    return render(request, 'pharmacie/thankyou.html')

def thankyouMessage(request):
    return render(request, 'pharmacie/thankyouMessage.html')

def about2(request):
    x = request.POST.get('lg')
    y = request.POST.get('pass')
    data = Login(username=x, password=y)
    data.save()
    return render(request, 'pharmacie/login.html')

def sessionCreate(request):
    nameOfSession = "userName"
    ### Creating sessions in Django ###
    request.session[nameOfSession] = "John Doe"
    request.session[nameOfSession] = "Jahn Doe"
    request.session.pop(nameOfSession, None)
    ### Reading sessions in Django ###
    username = "No user"
    if nameOfSession in request.session:
        username = request.session.get(nameOfSession)

    context = {"username":username}
    return render(request, 'pharmacie/testSession.html',context)