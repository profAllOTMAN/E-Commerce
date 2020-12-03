from django.contrib.auth.models import AbstractUser
from django.db import models




class category(models.Model):
    category_name = models.CharField(max_length=64,default=None)
    def __str__(self):
        return f" {self.category_name} "

class listing(models.Model):
    title = models.CharField(max_length=64,default=None)
    description = models.CharField(max_length=64 ,default=None)
    bid = models.IntegerField(default=None)
    url = models.CharField(max_length=64 ,default=None)
    category = models.ManyToManyField(category, blank=True, related_name="Category")
    def __str__(self):
        return f" {self.title} {self.description} ({self.bid})"

class bids(models.Model):
    bid = models.IntegerField(default=None)

class comment(models.Model):
    pass

class User(AbstractUser):
    pass