import datetime
from msvcrt import locking
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required  # Import this
from .forms import HotelForm, LoginForm
from .models import Hotel, Room ,Booking

# admin_app/views.py

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hotel_list')  # Ensure this matches the URL name
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'adminlogin.html', {'form': form})


@login_required
def hotel_list_view(request):
    active_hotels = Hotel.objects.filter(status='Active').order_by('name')
    draft_hotels = Hotel.objects.filter(status='Draft').order_by('name')
    return render(request, 'hotel_list.html', {
        'active_hotels': active_hotels,
        'draft_hotels': draft_hotels,
    })

def hotel_detail_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import HotelRegistrationForm, UserRegistrationForm
from .models import Hotel

@login_required
def register_hotel(request):
    if request.method == 'POST':
        hotel_form = HotelRegistrationForm(request.POST, request.FILES)
        user_form = UserRegistrationForm(request.POST)
        if hotel_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            hotel = hotel_form.save(commit=False)
            hotel.owner = user  # Correctly setting the owner attribute
            hotel.save()
            return redirect('hotel_list')  # Redirect to hotel
    else:
        hotel_form = HotelRegistrationForm()
        user_form = UserRegistrationForm()
    return render(request, 'register_hotel.html', {'hotel_form': hotel_form, 'user_form': user_form})

from .forms import RoomForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hotel, Room
from .forms import RoomForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hotel, Room
from .forms import RoomForm

@login_required
def add_room(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.hotel = hotel
            room.save()
            if hotel.status == 'pending':
                hotel.status = 'active'
                hotel.save()
            return redirect('hotel_detail', hotel_id=hotel.id)
        else:
            return render(request, 'add_room.html', {'form': form, 'hotel': hotel})
    
    else:
        form = RoomForm()
        return render(request, 'add_room.html', {'form': form, 'hotel': hotel})

    # Ensure the view always returns an HttpResponse
    return render(request, 'add_room.html', {'form': form, 'hotel': hotel})

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from .forms import HotelRegistrationForm, UserEditForm


@login_required
def edit_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    
    if request.method == 'POST':
        hotel_form = HotelForm(request.POST, request.FILES, instance=hotel)
        if hotel_form.is_valid():
            hotel_form.save()
            return redirect('hotel_detail', hotel_id=hotel.id)
    else:
        hotel_form = HotelForm(instance=hotel)
    
    return render(request, 'edit_hotel.html', {'hotel_form': hotel_form, 'hotel': hotel})

@login_required
def delete_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    
    # Ensure there are no active booking requests for any room before deleting
    if request.method == 'POST':
        if hotel.room_set.filter(booking__isnull=False).exists():
            # You may want to add a message here indicating that the hotel cannot be deleted
            return redirect('hotel_detail', hotel_id=hotel.id)
        hotel.delete()
        return redirect('hotel_list')
    
    return render(request, 'delete_hotel.html', {'hotel': hotel})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hotel, Room
from .forms import RoomForm
def view_hotel_rooms(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    hotel_rooms = hotel.rooms.all()
    return render(request, 'hotel_rooms.html', {'hotel': hotel, 'hotel_rooms': hotel_rooms})


    

