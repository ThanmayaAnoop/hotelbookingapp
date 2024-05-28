from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import GuestLoginForm

def guest_login_view(request):
    if request.method == 'POST':
        form = GuestLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('guest_home')  # Adjust redirect as needed
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = GuestLoginForm()
    return render(request, 'guestlogin.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def guest_home_view(request):
    return render(request, 'guesthome.html')

