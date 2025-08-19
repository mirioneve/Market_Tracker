from django.db import models
from phone_field import PhoneField
from address.models import AddressField

# Create your models here.
CATEGORY_CHOICE = (
    ("E", "Electornies"),
    ("C", "Clothing"),
    ("HG", "Home & Garden"),
    ("S", "Sports"),
    ("B", "Books"),
    ("F", "Foods"),
    ("O", "Others"),
)

class Product(models.Model):
    """A class to manage new products"""
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=50)
    description = models.TextField()
    image = models.ImageField()
    phone = PhoneField()
    address1 = AddressField()
    address2 = AddressField(related_name='+', blank=True, null=True)
   
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title