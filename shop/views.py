from django.shortcuts import render,redirect
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


