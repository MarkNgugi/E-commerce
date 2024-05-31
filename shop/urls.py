from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homemain,name='homemain'),
    path('shop/',views.shopmain,name='shopmain'),
    path('category/<slug:slug>/',views.category_details,name='category_details'),

    path('add_product',views.add_product,name='add_product'),
    path('success',views.successpage,name='successpage')

]