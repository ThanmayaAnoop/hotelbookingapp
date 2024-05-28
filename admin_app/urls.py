from django.urls import path
from .views import  hotel_list_view, login_view,  hotel_detail_view

urlpatterns = [
    path('login/', login_view, name='login'),
     path('hotel_list/', hotel_list_view, name='hotel_list'),
     path('hotel/<int:hotel_id>/', hotel_detail_view, name='hotel_detail')
]

