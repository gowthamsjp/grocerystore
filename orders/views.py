from django.shortcuts import render, HttpResponseRedirect
from .models import *
from ecommerce.models import Product
from django.contrib.auth.decorators import login_required
from ecommerce.views import *
from carts.views import *
from django.urls import reverse
from django.contrib.sessions.models import Session
import time
import math
from accounts.models import *
from accounts.forms import *
from .models import * 
from accounts.views import *
import decimal
# to create a new order
@login_required
def checkout(request):
    # To get the cart currently 
    try: 
            cart = Cart.objects.get(user = request.user, ordered=False)
    except: 
            cart = None
            return HttpResponseRedirect(reverse('cart'))

    #To get the order, if not create a new one
    try: 
        new_order  = Order.objects.get(user = request.user, cart=cart )
    except Order.DoesNotExist: 
        new_order = Order.objects.create(user = request.user,cart=cart)

    # To calculate all total of cart in checkout
    total = cart.total 
    new_order.subTotal = total
    new_order.save()

    finalTotal = decimal.Decimal(new_order.subTotal) + decimal.Decimal(new_order.subTotal) * decimal.Decimal(new_order.taxTotal)
    new_order.finalTotal = round(finalTotal,2)
    new_order.save()

# Get the address
    try: 
        address_added = request.GET.get("address_added")
    except: 
        pass

    if address_added is None: 
        address_form = add_address(request)
    else: 
        address_form = None 
   
    current_address = UserAddress.objects.filter(user=request.user)
    billing = UserAddress.objects.get_billing_address(user=request.user)

    # try: 
    #         billingFalse = UserAddress.objects.filter(user=request.user)
    # except:
    #         billingFalse="No address. Please Add !!!"
    

    order = Order.objects.get(user = request.user, cart=cart )
    context = {"address_form":address_form, "order": order, 
                "current_address": current_address, 'billing' : billing, 
    }
    template = 'checkout/checkout.html'
    return render(request,template,context)

def orders(request): 
    # Finshed order
    cart = Cart.objects.get(user = request.user, ordered=False)
    new_order  = Order.objects.get(user = request.user, cart=cart )
    new_order.status = "Pending"
    new_order.save()
    cart.ordered = True
    cart.save()

    request.session['key'] = 0

    return HttpResponseRedirect(reverse('homeMain'))
