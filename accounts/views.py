from django.shortcuts import render, get_object_or_404, reverse, redirect
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
# Import Booking model from models
from .models import Booking, UserProfile
from .forms import UpdateBookingDetails, EditProfileForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            )

class ServicesView(TemplateView):
    template_name = "services.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "services.html",
        )

class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "contact.html",
            )

class OnlineBookingView(View):
    template_name = "online_booking.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "online_booking.html",
            {
                "online_booking_active": "custom-red",
            }
        )

    def post(self, request):
        date = request.POST.get("date")
        time = request.POST.get("time")
        comments = request.POST.get("comments")

        online_booking = Booking.objects.create(
            booking_date=date,
            booking_time=time,
            user=request.user,
            booking_comments=comments
        )

        online_booking.save()

        return redirect(reverse('manage_booking'))

class CreateProfile(View):
    template_name = "create_profile.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_profile.html",
        )

    def post(self, request):
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        dog_name = request.POST.get("dog_name")
        tele = request.POST.get("phone_number")

        CreateUserProfile = UserProfile.objects.create(
            first_name=f_name,
            last_name=l_name,
            phone_number=tele,
            user=request.user,
        )

        CreateUserProfile.save()

        return redirect(reverse('home'))        
