from django import forms

from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
        email = forms.CharField(max_length=150, required=True)
        password = forms.CharField(widget=forms.PasswordInput, required=True)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nom = forms.CharField(max_length=100)
    # date_inscription = models.DateTimeField(auto_now_add=True)
    class Meta:
        model = Utilisateur
        fields = ['email', 'nom', 'password1', 'password2']
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
           raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return password2