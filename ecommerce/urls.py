from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from . import views
from .views import home, register, homeMain, about, signin, logout_views, product
urlpatterns = [
    # first page, before sign in
    path('', home, name='home'),
    # to introduce company
    path('about', about, name='about'),
    # to sign in
    path('signin', signin, name='signin'),
    #  to register
    path('register', register, name='register'),
    # to log out
    path("logout", logout_views, name="logout"),
    # this link is to display product after log in
    path('homeMain', homeMain, name="homeMain"),

    # to specific product, have a unique slug (slug is the unique code for a product), and id of product
    url(r'^product/(?P<slug>[\w-]+)/(?P<id>\d+)/$', product, name='product'),
    #     (?P<all_items>.*)
    #  if use "\d+" to make the url only digit:     (?P<id>\d+)

]
