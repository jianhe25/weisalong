from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'login_result': '',
        })
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phone = request.POST.get('phone', None)
        if username == None or password == None or phone == None:
            raise Http404

# only check whether username exists now
# TODO: switch to real logic later
        if authenticate(username = username):
            login_result = 'success'
        else:
            login_result = 'fail'

        return render(request, 'login.html', {
            'login_result': login_result,
        })
    else:
        raise Http404

def profile(request):
    return render(request, 'profile.html', {
    })

