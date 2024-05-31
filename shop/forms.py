from django import forms

class ProductSellForm(forms.form):
    category=forms.CharField()
    productname=forms.CharField(max_length=100)
    description=forms.TimeField()
    price=forms.DecimalField()
    stock=forms.PositiveIntegerField()
