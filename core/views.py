from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import TestForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html',{'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})