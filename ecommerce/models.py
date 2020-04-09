from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Product(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0.0)
    salePrice = models.DecimalField( decimal_places=2, max_digits=100, default=0.0)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # to make the title is unique if not, should choose another title to name because it will make slug unique
    class Meta:
        unique_together = ('title', 'slug')

    def get_price(self):
        return self.price
    # to get the link of a unique product
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='')
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title




# class Cart(models.Model):
#     creation_date = models.DateTimeField(verbose_name=_('creation date'))
# # for item
# class Product(models.Model):
#     title = models.CharField(blank=False, max_length=100)
#     price = models.FloatField
#     description = models.CharField(blank=False,max_length=1000)
#
#     # image = models.ImageField(upload_to ='./static/images/')
#     def __str__(self):
#         return self.user.title
#
# # for cart
# class OrderItem(models.Model):
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.title
#
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     items = models.ManyToManyField(OrderItem)
#     star_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.username
