from django import forms
from bugapp.models import Ticket

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class NewTicketForm(forms.Form):
    title = forms.CharField(max_length=240)
    description = forms.CharField(widget=forms.Textarea)