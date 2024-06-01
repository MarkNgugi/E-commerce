from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homemain,name='homemain'),
    path('shop/',views.shopmain,name='shopmain'),
    path('category/<slug:slug>/',views.category_details,name='category_details'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('add_product',views.add_product,name='add_product'),
    path('success',views.successpage,name='successpage'),

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),

]