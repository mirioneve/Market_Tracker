from django.db import models
from phone_field import PhoneField

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

class Item(models.Model):
    """A model to handle item"""
    title = models.CharField(max_length=200)
    seller = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self,):
        """Returning an item title"""
        return self.title

class Product(models.Model):
    """A class to manage new products"""
    title = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=50)
    description = models.TextField()
    image = models.ImageField()
    phone = PhoneField(default=2090768)
   
    is_active = models.BooleanField(default=True)
    
    class Mete:
        name_products = 'products'

    def __str__(self):
        return f"{self.description[:50]}...."