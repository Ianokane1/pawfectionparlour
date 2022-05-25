from django.shortcuts import render
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            {
                "home_active": "",
            }
        )