from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import TestForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def home(request):
    return render(request, 'core/home.html')


def profissionais(request):
    if request.method == 'POST':
        form = TestForm(request.Post)

        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = TestForm()
    return render(request, 'core/profissionais.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login_view.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
