from django import forms
from .models import ContactMe

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ['name', 'email', 'Subject', 'comment']  # Add any fields you want in the form
