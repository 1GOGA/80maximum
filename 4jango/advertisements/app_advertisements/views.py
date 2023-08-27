from django.shortcuts import render

# Create your views here.


def example(requests):
    return render(requests, "index.html")

def top_sellers(requests):
    return render(requests, "top-sellers.html")

