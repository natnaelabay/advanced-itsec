from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user.forms import UserForm, LoginForm

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserForm()
        return render(request, "user/register.html", {
            "form": form
        })
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def dashboard(request):
    return render(request, 'user/dashboard.html')