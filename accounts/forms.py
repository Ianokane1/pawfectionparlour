from .models import Booking, UserProfile
from django import forms
from django.forms import ModelForm, CharField, TextInput

class UpdateBookingDetails(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'booking_date', 'booking_time')

class EditProfileForm(forms.ModelForm):

    phone_number = CharField(widget=TextInput(attrs={'type': 'number'}))
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'dog_name', 'phone_number')            