"""itsec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.http import HttpResponseForbidden, FileResponse
import os
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden, HttpResponseNotFound, FileResponse
import os

def download_feedback(request, feedback_id):
    feedback = Feedback.objects.get(pk=feedback_id)

    if feedback.user != request.user:
        return HttpResponseForbidden("Bad Request.")

    file_path = feedback.pdf_file.path

    if file_path and os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
            response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(file_path) + '"'
            return response

    return HttpResponseNotFound("File not found.")


from django.shortcuts import render, redirect
from user.views import guest_only

def home_view(request):
    return redirect("login")    

urlpatterns = [
    path('', home_view),
    path('', include('user.urls')),
    path('dashboard/', include('review.urls')),
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)