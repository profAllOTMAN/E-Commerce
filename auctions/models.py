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
    url = models.CharField(max_length=200 )
    categorys = models.ForeignKey(category, on_delete=models.CASCADE, related_name="category")
    sat = models.TextChoices('statu','active no_active')
    status = models.CharField(blank=True, choices=sat.choices, max_length=10)
    def __str__(self):
        return f" {self.title} {self.description} ({self.bid}) {self.status} "




class bids(models.Model):
    bid = models.IntegerField()

class comment(models.Model):
    pass

class User(AbstractUser):
    pass

class watchlist(models.Model):
    user_name = models.CharField(max_length=64)
    listings = models.ManyToManyField(listing,blank=True ,related_name= "listing_add")
    def __str__(self):
        return f" {self.user_name} {self.listings} "
