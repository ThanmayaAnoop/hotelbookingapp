from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.guest_login, name='guest_login'),
]

