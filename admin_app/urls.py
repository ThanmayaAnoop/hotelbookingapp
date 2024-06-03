from django.urls import path
from .views import  add_room, delete_hotel, edit_hotel, hotel_list_view, login_view,  hotel_detail_view, register_hotel, view_hotel_rooms

urlpatterns = [
    path('login/', login_view, name='login'),
     path('hotel_list/', hotel_list_view, name='hotel_list'),
     path('hotel/<int:hotel_id>/', hotel_detail_view, name='hotel_detail'),
     path('register_hotel/', register_hotel, name='register_hotel'),
     path('hotel/<int:hotel_id>/edit/', edit_hotel, name='edit_hotel'),
    path('hotel/<int:hotel_id>/delete/', delete_hotel, name='delete_hotel'),
    path('hotel/<int:hotel_id>/add_room/', add_room, name='add_room'),
    path('hotel/<int:hotel_id>/rooms/', view_hotel_rooms, name='view_hotel_rooms'),
]

