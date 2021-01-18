from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def autentificare(request):
    if request.method == 'GET':

        return render(request, 'autentificare.html')

    else:
        try:

            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password'], email=request.POST['email'])
            user.save()
            login(request, user)
            return redirect('home')
        except IntegrityError:
            return render(request, 'autentificare.html', {'error': 'Contul exista deja!'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginpage(request):
    if request.method == 'GET':

        return render(request, 'loginpage.html')

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
        if user is None:
            return render(request, 'loginpage.html', {'error': 'Contul sau parola nu se potrivesc!'})
        else:
            login(request, user)
            return redirect('home')
