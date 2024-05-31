from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homemain,name='homemain'),
    path('shop/',views.shopmain,name='shopmain')

]