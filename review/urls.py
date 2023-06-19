from review.views import feedback, dashboard, edit_feedback, download_view
from django.urls import path

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("feedback/", feedback, name="feedback"),
    path("feedback/edit/<uuid:id>/", edit_feedback, name="edit-feedback"), 
    path('download/<uuid:id>/', download_view, name='download_file'),
]