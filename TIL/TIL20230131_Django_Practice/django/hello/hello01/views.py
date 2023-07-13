from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("<h1><a href='/'>A tag - Hello, Test!</a></h1>")
