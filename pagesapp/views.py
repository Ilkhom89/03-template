from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class PlatPageView(TemplateView):
    template_name = 'plat.html'

class PractPageView(TemplateView):
    template_name = 'pract.html'
