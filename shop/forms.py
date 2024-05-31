from django.forms import ModelForm
from django import forms
from .models import *

class ProductSellForm(ModelForm):
    class Meta:
        model=Product
        exclude=['slug','available','created','updated']
