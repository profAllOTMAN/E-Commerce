from django.contrib.auth.models import AbstractUser
from django.db import models




class category(models.Model):
    categoryname = models.CharField(max_length=64)
    def __str__(self):
        return f" {self.categoryname} "

class listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64 )
    bid = models.IntegerField()
    url = models.CharField(max_length=64 )
    categorys = models.ForeignKey(category, on_delete=models.CASCADE, related_name="category")
    def __str__(self):
        return f" {self.title} {self.description} ({self.bid}) "




class bids(models.Model):
    bid = models.IntegerField()

class comment(models.Model):
    pass

class User(AbstractUser):
    pass