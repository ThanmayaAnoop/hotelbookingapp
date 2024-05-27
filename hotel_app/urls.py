from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.hotel_login, name='hotel_login'),
]

