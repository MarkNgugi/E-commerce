from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    homepage = "<H1>CONTENT WILL BE ADDED SOON<H1>"
    return HttpResponse(homepage)
