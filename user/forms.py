from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User
from captcha.fields import ReCaptchaField

class GenericEmailField(forms.EmailField):
    default_error_messages = {
        'invalid': 'Please enter a valid email address.',
        'required': 'This field is required.',
        'unique': 'This email is already taken.',
    }

class GenericEmailLoginField(forms.EmailField):
    default_error_messages = {
        'invalid': 'Please enter a valid email address.',
        'required': 'This field is required.',
        'unique': 'This email is already taken.',
    }

class UserForm(UserCreationForm):
    email = GenericEmailField(required=True,widget= forms.EmailInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField( min_length=9, max_length=128,label="Password", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'auto-complete': "false"}))
    password2 = forms.CharField(min_length=9, max_length=128,label="Confirm", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'auto-complete': "false"}))
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', "captcha"]
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class AuthForm(AuthenticationForm):
    username = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=9, max_length=128, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'auto-complete': "false"}))
    captcha = ReCaptchaField(required=True)

    error_messages = {
        'invalid_login': "Invalid email address or password. Please try again.",
        'inactive': "This account is inactive.",
    }