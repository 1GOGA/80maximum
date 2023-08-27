from django.urls import path
from .views import domashka



urlpatterns = [
    path("lesson_4/", domashka),
    ]