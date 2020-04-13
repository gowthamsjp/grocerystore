from django.db import models
from carts.models import Cart
from ecommerce.models import User
from datetime import datetime
from django.conf import settings
import uuid

# Python tuples
STATUS_CHOICES = (
    ("Started", "Started"),
    ("Pending", "Pending"), 
    ("Abandoned","Abandoned" ),
    ("Finished", "Finished"), 
)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, )# total price with tax
    subTotal = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00) #  total price without tax
    taxTotal = models.DecimalField(max_digits=1000, decimal_places=2, default=0.09) #  tax price
    finalTotal = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00) #  final total 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    start_date  = models.DateTimeField(auto_now=False, auto_now_add=True) 
    ordered_date = models.DateTimeField(auto_now=True, auto_now_add=False) #last day of updating the cart that means checkout date

    def __unicode__(self):
        return self.order_id