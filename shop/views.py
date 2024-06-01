from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import ProductSellForm

def homemain(request):
    context={}
    return render(request,'shop/home.html',context)

def shopmain(request):
    categories = Category.objects.all()
    context = {'categories':categories}

    return render(request,'shop/shopmain.html',context)

def category_details(request,slug):
    category = Category.objects.get(slug=slug)
    products=category.products.all()
    context={
        'products':products,
        'categories':category
             }
    return render(request,'shop/category_details.html',context)

def add_product(request):

    if request.method=='POST':
        productsellform=ProductSellForm(request.POST)
        if productsellform.is_valid():
            product=productsellform.save()
            return redirect('successpage')
        else:
            pass
    else:
        productsellform=ProductSellForm()

    context={'productsellform':productsellform}
    return render(request,'shop/sellproducts.html',context)

def successpage(request):
    context={}
    return render(request,'shop/sellsuccess.html',context)


def get_cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    return cart

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = get_cart(request)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')

def cart_detail(request):
    cart = get_cart(request)
    total_price = sum(item.get_total_price() for item in cart.items.all())
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'total_price': total_price})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


