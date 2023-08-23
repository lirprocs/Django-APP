from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def support(request):
    return HttpResponse('<h4>Тут скоро будет поддержка<h4>')


def about(request):
    return render(request, 'main/about.html')



