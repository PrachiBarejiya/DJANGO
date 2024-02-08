from django.db import models
from django import forms

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price']