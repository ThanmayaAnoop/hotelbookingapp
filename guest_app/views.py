from django.shortcuts import render

def guest_login(request):
    return render(request, 'login.html')
