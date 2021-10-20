from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView

from users.forms import ProfileModelForm
from users.models import ProfileModel


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    form_class = ProfileModelForm

    def get_success_url(self):
        return reverse('profile:home')

    def get_object(self, queryset=None):
        profile, created = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile
