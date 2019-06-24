from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from core.forms import CustomUserCreationForm


def home(request):
    return render(request, 'core/home.html')

@login_required(login_url='/signup/')
def profissionais(request):
    return render(request, 'core/profissionais.html')


def signup(request):
    if request.method == 'POST':
        form1 = CustomUserCreationForm(request.POST)
        if form1.is_valid():
            user = form1.save()
            login(request, user)
            return redirect('home')
    else:
        form1 = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'user_form': form1})


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
