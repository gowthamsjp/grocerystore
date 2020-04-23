from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include, re_path
from . import views
from .views import register, homeMain, about, signin, logout_views, UniqueProduct, search, category, contact
from carts.views import cart, update_cart, delete_cart
from orders.views import checkout, orders
from accounts.views import add_address, profile



urlpatterns = [ 
    # first page, before sign in
    # path('', home, name='home'),
    path('', homeMain, name="homeMain"),
    # to introduce company
    path('about', about, name='about'),
    # to sign in
    path('signin', signin, name='signin'),
    #  to register
    path('register', register, name='register'),
    # to log out
    path("logout", logout_views, name="logout"),
    #to contact us
    path("contact",contact, name="contact"),

    url(r'^category/$',category, name="category"),

    # this link is to display product after log in
    # This link is for searching, s for search
    url(r'^s/$',search, name='search'),
    # to specific product, have a unique slug (slug is the unique code for a product), and id of product
    # url(r'^product/(?P<slug>[\w-]+)/(?P<id>\d+)/$', product, name='product'),
    #     (?P<all_items>.*)
    #  if use "\d+" to make the url only digit:     (?P<id>\d+)
    path('<slug:slug>UniqueProduct', UniqueProduct , name='product'),
    path('yourCart', cart, name='cart'),
    url(r'^yourCart/(?P<slug>[\w-]+)/$',update_cart, name='update_cart'),
    url(r'^yourCart/delete/(?P<slug>[\w-]+)/$',delete_cart, name='delete_cart'),
    
    path('checkout', checkout , name='checkout'),
    path('orders', orders , name='orders'),
    path('add_address', add_address, name="add_address"), 
    path('profile', profile, name="profile"), 

    # path('defaultAddress', defaultAddress, name='defaultAddress')
]
