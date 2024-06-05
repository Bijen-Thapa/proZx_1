from django.shortcuts import render

from django.http import HttpResponse

about = [
    {"id": 1, "name":"LMao"},
    {"id": 2, "name":"Lo"},
    {"id": 3, "name":"Lol"},
]

def home(request): 
    return render(request, "base/home.html")

def about(request): 
    content = {"detail":about}
    return render(request, "base/about.html", content)

def registration(request):
    return render(request, "base/registration.html")
