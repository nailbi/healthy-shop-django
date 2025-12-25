from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    ingredients = models.TextField()
    nutrition = models.CharField(max_length=200)  # КБЖУ
    allergens = models.CharField(max_length=200)

    image = models.ImageField(upload_to='products/')
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
