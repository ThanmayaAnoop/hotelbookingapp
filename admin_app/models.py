from django.db import models

class Hotel(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Draft', 'Draft'),
    )
    
    name = models.CharField(max_length=100)
    address = models.TextField(default='Not Provided')  # New field
    photo = models.ImageField(upload_to='hotel_photos/',default='default_hotel.jpg')  # New field
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    star_rating = models.PositiveIntegerField()
    owner_name = models.CharField(max_length=100,  default='Not Provided')  # New field
    owner_photo = models.ImageField(upload_to='owner_photos/' , default='default_owner.jpg')  # New field
    owner_email = models.EmailField(default='noemeail@example.com')  # New field
    owner_phone = models.CharField(max_length=15,default='0000000000')  # New field

    def __str__(self):
        return self.name

    def total_rooms(self):
        return self.room_set.count()

    def total_occupancy(self):
        return sum(room.occupancy for room in self.room_set.all())

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,  default='Standard Room')  # New field
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)  # New field
    max_occupancy_adults = models.PositiveIntegerField(default=2)  # New field
    max_occupancy_children = models.PositiveIntegerField(default=0)  # New field
    occupancy = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.hotel.name} Room'

# admin_app/models.py

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    def __str__(self):
        return f'Booking at {self.hotel.name} for {self.room.name}'
