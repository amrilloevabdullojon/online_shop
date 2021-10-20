from django.forms import ModelForm

from pages.models import ContactModel
from django import forms


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created_at']
