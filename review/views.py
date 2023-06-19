from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from review.forms import FeedbackForm
from review.models import Feedback
from django_ratelimit.decorators import ratelimit

@ratelimit(key='user_or_ip', rate='10/m')
@login_required(login_url="login")
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user            
            feedback.save()
            return redirect("dashboard")
    else:
        form = FeedbackForm()
    return render(request, "review/add.html", {"form": form})


@ratelimit(key='user_or_ip', rate='10/m')
@login_required(login_url="login")
def dashboard(request):
    data = Feedback.objects.filter(user=request.user)
    return render(request, "review/dashboard.html", {"data": data, "user" : request.user.full_name})

@ratelimit(key='user_or_ip', rate='10/m')
@login_required(login_url="login")
def edit_feedback(request, id):
    instance = get_object_or_404(Feedback, id=id)
    if request.method == "GET":    
        form = FeedbackForm(instance=instance)
        return render(request, "review/edit.html", {"form": form})
    else:
        form = FeedbackForm(request.POST,  request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    
    return render(request, "review/edit.html", {"form": form})

from django.http import FileResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Feedback
from django.conf import settings

@ratelimit(key='user_or_ip', rate='10/m')
@login_required(login_url="login")
def download_view(request, id):
    feedback = get_object_or_404(Feedback, id=id)
    try:
        feedback = Feedback.objects.get(id=id)
        if feedback.user.id != request.user.id:
            return HttpResponseForbidden()
        if not feedback.pdf_file:
            return HttpResponseBadRequest() 
    except Feedback.DoesNotExist:
        return HttpResponseBadRequest()
    file_path = feedback.pdf_file.path
    file_path = file_path.replace(settings.MEDIA_ROOT, "")
    file_path = file_path.replace("\\", "/")

    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{feedback.pdf_file.name}"'
    return response