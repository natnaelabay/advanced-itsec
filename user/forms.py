from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User
from captcha.fields import ReCaptchaField

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', "captcha"]
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class LoginForm(AuthenticationForm):
    pass