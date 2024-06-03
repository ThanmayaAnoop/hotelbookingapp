from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Hotel, Room


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            'name', 'address', 'photo', 'status', 'star_rating',
            'owner_name', 'owner_photo', 'owner_email', 'owner_phone'
        ]

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'entry_fee', 'max_occupancy_adults', 'max_occupancy_children', 'occupancy']
        


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class HotelRegistrationForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'address', 'photo', 'star_rating']
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


