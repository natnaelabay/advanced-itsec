from review.views import feedback, dashboard, edit_feedback
from django.urls import path


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("feedback/", feedback, name="feedback"),
    # FIXME: Check if there is a better way of passing params
    path("feedback/edit/<uuid:id>/", edit_feedback, name="edit-feedback")
]