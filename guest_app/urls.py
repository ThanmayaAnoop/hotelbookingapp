from django.urls import path
from .views import guest_login_view, guest_home_view

urlpatterns = [
    path('login/', guest_login_view, name='guest_login'),
    path('home/', guest_home_view, name='guest_home'),
]

