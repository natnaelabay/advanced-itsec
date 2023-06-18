from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from review.forms import FeedbackForm
from review.models import Feedback


@login_required(login_url="login")
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = FeedbackForm(request.POST, request.FILES)
        return render(request, "review/add.html", {"form": form})


@login_required(login_url="login")
def dashboard(request):
    data = Feedback.objects.all()
    return render(request, "review/dashboard.html", {"data": data})


@login_required(login_url="login")
def edit_feedback(request, id):
    if request.method == "GET":    
        instance = get_object_or_404(Feedback, id=id)
        data = FeedbackForm(instance=instance)
        return render(request, "review/edit.html", {"form": data})
    else:
        # post
        return redirect("dashboard")