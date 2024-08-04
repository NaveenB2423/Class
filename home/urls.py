from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index' ),
    path('products/<str:menu>',main_products,name='main_products'),
    path('products/<str:main_menu>/<str:sub_menu>',sub_products,name='sub_products'),
    path('about/',about_us, name='about_us'),
    path('contact/',contact_us, name='contact_us'),
    path('login/',customer_login, name='customer_login'),
    path('logout/',customer_logout,name='customer_logout'),
    path('signup/',customer_signup, name='customer_signup'),
    path('products/',products,name='products'),
    path('product-details/<str:name>',product_details,name='product_details'),
    path('shopping-cart/',shopping_cart,name='shopping_cart'),
    path('blog/',blog,name='blog'),
    path('blog-details/',blog_details,name='blog_details'),
    path('cart/', cart,name='cart' ),
    path('custompage/',custompage,name='custompage')
]