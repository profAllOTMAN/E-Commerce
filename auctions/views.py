from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User , comment , bids , listing , category ,  watchlist


def index(request):
    items= listing.objects.filter(status="active")
    return render(request, "auctions/index.html",{
        "listing":items
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
        items.status="active"
        #creator of this listing
        items.author = request.user.get_username()
        items.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request,"auctions/create_listing.html",{
        "categorys":category.objects.all()
        })




def watchlist_page(request):
    try:
        name_user = User.objects.get(username=request.user.get_username())
        all_listings = watchlist.objects.get(user_name=name_user)
        return render(request,"auctions/watchlist.html",{
            "list_watch": all_listings.listings.all()
        })
    except:
        watchlist.objects.create(user_name=name_user)
        all_listings = watchlist.objects.get(user_name=name_user)
        return render(request,"auctions/watchlist.html",{
            "list_watch": all_listings.listings.all()
        })
    
def page_listing(request,listing_id):
    Listing =listing.objects.get(pk=listing_id)
    name_user = User.objects.get(username=request.user.get_username())
    start_bid = Listing
    bidds=bids()
    bidoflisting = bids.objects.get(pk=listing_id)
   # if this watchlist exist
    try:
        # for closed the listing 
        

        # get exactly watchlist related to this user 
        watchlist_name = watchlist.objects.get(user_name=name_user)
        # recieving data ba a q;  queryset 
        if request.method == "POST":

            if request.POST["q"] == "closed":
                
                user_win = bidoflisting.user_name
                Listing.status="no_active"
                Listing.save()
                return render(request,"auctions/page_listing.html",{
                    "listing":Listing,
                    "user_win":user_win
                    })
            # user bided conditions 
            if request.POST["q"] == "bid" :
                bides = int(request.POST["bid"])
                if bides > start_bid.bid :
                    start_bid.bid = bides
                    bidds.user_name= name_user
                    bidds.bid = bides
                    bidds.listings =Listing
                    start_bid.save()
                    bidds.save()
                    return render(request,"auctions/page_listing.html",{
                        "listing":Listing,
                        })
                else:
                    bidds.bid = start_bid.bid
                    error = True
                    return render(request,"auctions/page_listing.html",{
                        "listing":Listing,
                        "eror":error,
                        })
            q =  request.POST["q"]
            if q == "add":
                watchlist_name.listings.add(Listing)
                return HttpResponseRedirect(reverse("watchlist"))
            elif q == "remove":
                watchlist_name.listings.remove(Listing)
                return HttpResponseRedirect(reverse("index"))
        return render(request,"auctions/page_listing.html",{
            "listing":Listing,
            "list_watch": watchlist_name.listings.filter(title=Listing.title),
            "user_won":bidoflisting.user_name
            })
            
        
    except watchlist.DoesNotExist:
        watchlist.objects.create(user_name=name_user)
        watchlist_name = watchlist.objects.get(user_name=name_user)
        return HttpResponseRedirect(reverse("index"))

    
    


    

"""
def bided(request,listing_id):
    Listing =listing.objects.get(pk=listing_id)
    name_user = User.objects.get(username=request.user.get_username())
    start_bid = Listing
    bidds=bids()
    if request.method == "POST":
        bides = int(request.POST["bid"])
        if bides > start_bid.bid :
            start_bid.bid = bides
            bidds.user_name= name_user
            bidds.bid = bides
            bidds.listings =Listing
            start_bid.save()
            bidds.save()
            return HttpResponseRedirect(reverse("watchlist"))
        else:
            bidds.bid = start_bid.bid
            return render(request,"auctions/page_listing.html",{
                "error":"try agin bide greater then "
                })
    return render(request,"auctions/page_bid.html",{
        "listing":Listing,
        })
                        

watchlist_name = watchlist.objects.get(user_name=name_user)

    return render(request,"auctions/page_listing.html",{
            "listing":Listing,
            "list_watch": watchlist_name.listings.all()
        })

    try: 
        watchlist_name = watchlist.objects.get(user_name=name_user)
        return watchlist_name
    except watchlist_name.DoesNotExist:
        watchlist.objects.create(user_name=name_user)
        watchlist_name = watchlist.objects.get(user_name=name_user)
        return watchlist_name

 name_user = User.objects.get(username=request.user.get_username())
    watchlist_name = watchlist.objects.filter(user_name=name_user)

    if request.method == "POST":
        
        q =  request.POST["q"]
        if q == "add":
            watchlist_name.listings.add(Listing)
            return HttpResponseRedirect(reverse("watchlist"))
        elif q == "remove":
            watchlist_name.listings.remove(Listing)
            return HttpResponseRedirect(reverse("index")) 

if q == "add":
            list_watch.append(Listing)
            return render(request,"auctions/watchlist.html",{
                "listingwatch":list_watch
            })
        elif q == "remove":
            return render(request,"auctions/page_listing.html")
listOfactiv = [] 
def active_listing(request):
    allListings = listing.objects.all()
    for ele in allListings:
        if ele.status == "active":
            listOfactiv.append(ele)
        elif:
            listOfactiv.remove(ele)
    return render(request,"auctions/active_listing.html",{
        "listingactive": listOfactiv
    })

categorys= category.objects.get(pk=int(request.POST["categroy"]))
        listing(request,title,description,bid,url,categor)
        listing.save()
"""