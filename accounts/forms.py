from django.forms import CharField, TextInput
from .models import Booking, UserProfile
from django import forms

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