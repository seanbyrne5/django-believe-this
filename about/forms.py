from django.apps import AppConfig
from django import forms

class CollaborateForm(forms.Form):
    # Your form fields here
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class AboutConfig(AppConfig):
    """
    Provides primary key type for about app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'