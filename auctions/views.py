from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Advert, Bid, Comment


def index(request):
    advertisements = Advert.objects.all().order_by("-created")

    if request.GET.get("category"):
        category = request.GET.get("category")

        return render(request, "auctions/index.html", {
                "advertisements": advertisements,
                "category": category
            })

    return render(request, "auctions/index.html", {
        "advertisements": advertisements,
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


@login_required
def create(request):
    user = request.user.username
    
    if request.method == "GET":
        return render(request, "auctions/create.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        image_url = request.POST.get("image")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = request.POST.get("category")

        ad = Advert(title=title, description=description, image=image_url, category=category)
        ad.save()
        bid = Bid(user=user, amount=price, advertisement=ad)
        bid.save()

        return HttpResponseRedirect(reverse("index"))


def advertisement(request, id):
    user = request.user.username
    ad = Advert.objects.get(id=id)
    highest_bid = ad.bid.last().amount
    comments = ad.comments.all().order_by("-date")
    
    user_obj = User.objects.get(username=user)
    current_user_saved = ad.saved.filter(username=user)  # QuerySet

    if request.GET.get("q") == "watchlist":
        if current_user_saved:
            ad.saved.remove(user_obj)
        else:
            ad.saved.add(user_obj)
        return redirect("advertisement", id=id)

    if request.GET.get("q") == "close":
        ad.active = False
        ad.save()
        return redirect("advertisement", id=id)

    if request.POST.get("comment"):
        text = request.POST.get("comment")
        new_comment = Comment(user=user, text=text, advertisement=ad)
        new_comment.save()
        return redirect("advertisement", id=id)

    
    elif request.POST.get("amount"):
        new_amount = request.POST.get("amount")
        bid = Bid(user=user, amount=new_amount, advertisement=ad)
        bid.save()

        return redirect("advertisement", id=id)

    return render(request, "auctions/advertisement.html", {
        "advert": ad,
        "min_bid": highest_bid + 1,
        "username": user,
        "comments": comments,
        "id": id
        })

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "auctions/profile.html", {
        "profile": user
        })

@login_required
def watchlist(request):
    user = request.user.username
    ads = Advert.objects.all().order_by("-created")

    return render(request, "auctions/watchlist.html", {
        "advertisements": ads,
        "username": user
        })