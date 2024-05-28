from django.contrib import admin
from .models import Hotel, Room , Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'star_rating')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'occupancy')

 
admin.site.register(Booking)

