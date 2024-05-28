import datetime
from msvcrt import locking
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required  # Import this
from .forms import LoginForm
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
@login_required
def hotel_detail_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)
    today = datetime.date.today()
    active_bookings_today = Booking.objects.filter(hotel=hotel, checkin_date=today).count()
    total_bookings = Booking.objects.filter(hotel=hotel).count()
    
    return render(request, 'hotel_detail.html', {
        'hotel': hotel,
        'rooms': rooms,
        'active_bookings_today': active_bookings_today,
        'total_bookings': total_bookings,
    })