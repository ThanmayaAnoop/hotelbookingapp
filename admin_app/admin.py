from django.contrib import admin
from .models import Hotel, Room , Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'status')
    search_fields = ('name', 'address')
    list_filter = ('status',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'entry_fee', 'hotel')
    list_filter = ('hotel',)

 
admin.site.register(Booking)

