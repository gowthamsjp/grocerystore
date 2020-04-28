from django.db import models
from ecommerce.models import Product, User
from datetime import datetime
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from localflavor.us.models import USStateField


# class UserAddressManager(models.Manager):
#     def get_billing_address(self,user):
#         return super(UserAddressManager, self).filter(billing=True).filter(user=user)   

class UserAddress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    address = models.CharField(max_length=120, null=False )
    city = models.CharField(max_length=50,)
    state = USStateField(null=True)
    zipcode = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=17, ) # validators should be a list
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # billing = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.user.username
    def get_address(self):
         return "%s, %s, %s, %s" %(self.address, self.city, self.state, self.zipcode)

    # objects = UserAddressManager()

# class UserDefaultAddress(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, )
#     shipping = models.OneToOneField(UserAddress, on_delete=models.CASCADE, 
#                         blank =True, null=True, related_name="user_default_address")

#     def __unicode__(self):
#         return self.user.username
