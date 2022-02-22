from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="homepage"),
    path("subjects/<id>", views.view_subject, name="view_subject")
]