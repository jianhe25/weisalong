from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def login(request):
    return render(request, 'login.html', {
    })

