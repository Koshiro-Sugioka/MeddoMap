from django import forms
from .models import Trip, Place
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['start_date_time', 'end_date_time', 'trip_name']
        widgets = {
            'start_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # Add other customizations here
        }

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['place_name']

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

