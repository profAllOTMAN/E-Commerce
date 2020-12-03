from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User , comment , bids , listing , category


def index(request):
    items= listing.objects.all()
    return render(request, "auctions/index.html",{
        "listing":items,
        
       
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def creat_listing(request):
    items=listing()
    if request.method == "POST":
        categorry= category.objects.get(pk=int(request.POST["categroy"]))
        items.title = request.POST["title"]
        items.description = request.POST["descrption"]
        items.bid = request.POST["bid"]
        items.url = request.POST["url"]
        items.categorys= categorry
        items.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request,"auctions/create_listing.html",{
        "categorys":category.objects.all()
        })

"""
categorys= category.objects.get(pk=int(request.POST["categroy"]))
        listing(request,title,description,bid,url,categor)
        listing.save()
"""