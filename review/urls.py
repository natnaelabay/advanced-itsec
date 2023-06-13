from review.views import my_view


from django.urls import path


urlpatterns = [
    path("", my_view)
]