from django.urls import path
from .views import hotel_home_view, hotel_login_view

urlpatterns = [
    path('login/', hotel_login_view, name='hotel_login'),
    path('home/', hotel_home_view, name='hotel_home'),
]

