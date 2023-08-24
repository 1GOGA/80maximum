from django.urls import path
from .views import example
from .views import lesson


urlpatterns = [
    path("", example),
    path("example/", example),
    path("lesson_4/", lesson ),
    ]