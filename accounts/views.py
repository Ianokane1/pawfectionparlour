from django.shortcuts import render, get_object_or_404, reverse, redirect
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView
# Import Booking model from models
from .models import Booking, UserProfile

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