from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path('ExchangeHub/', views.ExchangeHub, name = 'ExchangeHub'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('loading/', views.loading, name="loading"),
    path('home/', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('profile/', views.profile, name="profile"),
    path('contacts/', views.contacts, name="contacts"),
    path('sell/', views.sell, name="sell"),
    path('settings/', views.settings, name="settings"),
    path('moreinfo/', views.moreinfo, name="moreinfo")
]


