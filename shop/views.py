from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def homemain(request):
    context={}
    return render(request,'shop/home.html',context)

def shopmain(request):
    categories = Category.objects.all()
    context = {'categories':categories}

    return render(request,'shop/shopmain.html',context)

def sellproducts(request):
    context={}
    return render(request,'shop/sellproducts.html',context)
    



