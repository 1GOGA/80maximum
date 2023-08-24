<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def example(requests):
    return HttpResponse("Чё зашел, тут ничего интерестного")

def lesson(requests):
=======
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def example(requests):
    return HttpResponse("Чё зашел, тут ничего интерестного")

def lesson(requests):
>>>>>>> be5f2ae41295b9a1f36d2e21ca7a3ceefa7d69ae
    return HttpResponse("Домашка по 4 занятию")