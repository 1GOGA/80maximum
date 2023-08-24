<<<<<<< HEAD
from django.urls import path
from .views import example
from .views import lesson


urlpatterns = [
    path("", example),
    path("example/", example),
    path("lesson_4/", lesson ),
=======
from django.urls import path
from .views import example
from .views import lesson


urlpatterns = [
    path("", example),
    path("example/", example),
    path("lesson_4/", lesson ),
>>>>>>> be5f2ae41295b9a1f36d2e21ca7a3ceefa7d69ae
    ]