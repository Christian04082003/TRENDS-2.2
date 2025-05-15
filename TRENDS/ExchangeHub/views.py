from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    # Your view logic here
    return render(request, 'home.html')


def ExchangeHub(request):
  return render(request, "login.html")

def loading(request):
    return render(request, "loading.html")

def cart(request):
  return render(request, "cart.html")

def wishlist(request):
  return render(request, "wishlist.html")


def profile(request):
  return render(request, "profile.html")

def contacts(request):
  return render(request, "contacts.html")

def sell(request):
  return render(request, "sell.html")

def settings(request):
  return render(request, "settings.html")

def moreinfo(request):
  return render(request, "moreinfo.html")





