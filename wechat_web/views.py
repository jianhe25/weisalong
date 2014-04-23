from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
import time

def login(request):
    time.sleep(3)
    return HttpResponse("hello world!", content_type="text/plain")

