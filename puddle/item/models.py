from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Category(models.Model):
    # Define the Category model to represent a category of items.
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name 
    
    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'

class Item(models.Model):

    # Define the Item model to represent an item for sale.
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name