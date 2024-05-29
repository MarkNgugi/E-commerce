from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def homecategories(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'shop/home.html',context)



