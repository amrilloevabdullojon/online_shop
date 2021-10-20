from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class LoginView(TemplateView):
    template_name = 'registration/login.html'


class RegisterView(TemplateView):
    template_name = 'registration/registration_form.html'
