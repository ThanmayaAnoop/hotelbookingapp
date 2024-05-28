from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import HotelLoginForm

def hotel_login_view(request):
    if request.method == 'POST':
        form = HotelLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hotel_home')  # Adjust redirect as needed
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = HotelLoginForm()
    return render(request, 'hotellogin.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def hotel_home_view(request):
    return render(request, 'hotelhome.html')
