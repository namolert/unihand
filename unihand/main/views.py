from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def home(request: HttpRequest):
    return render(request, "main/home.html")
    # return HttpResponse('Hello')