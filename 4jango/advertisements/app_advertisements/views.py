from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def example(requests):
    return HttpResponse("Чё зашел, тут ничего интерестного")

def lesson(requests):
    return HttpResponse("Домашка по 4 занятию")