from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user.forms import UserForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



from django.shortcuts import redirect
from functools import wraps

def guest_only(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Redirect to the desired URL for authenticated users
        return view_func(request, *args, **kwargs)
    return wrapped_view

@guest_only
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

@guest_only
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard') 
    else:
        form = AuthenticationForm(request)
    return render(request, 'user/login.html', {'form': form})

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")