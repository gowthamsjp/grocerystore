from django.shortcuts import render
from django.conf import settings
import stripe 
from django.contrib.auth.signals import user_logged_in
from .models import UserStripeID
from ecommerce.models import Product, User

stripe.api_key = settings.STRIPE_SECRET_KEY
# To create stripe account , adn stripe Id in database
def get_or_create_stripe(sender, user, *args, **kwargs):
    try:
        user_stripe =  UserStripeID.objects.get(user=user)
    except UserStripeID.DoesNotExist:
        customer = stripe.Customer.create( email = user.email)
        new_user_stripe = UserStripeID.objects.create(user = user, stripe_id = customer.id)
    except: 
        pass   
user_logged_in.connect(get_or_create_stripe)
