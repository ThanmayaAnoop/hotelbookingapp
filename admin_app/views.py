from django.shortcuts import render

def admin_login(request):
    return render(request, 'login.html')
