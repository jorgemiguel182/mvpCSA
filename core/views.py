from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
#from core.forms import CustomUserCreationForm
from core.forms import  UserProfileForm, UserModelForm

from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy



def home(request):
    return render(request, 'core/home.html')

@login_required(login_url='/signup/')
def profissionais(request):
    return render(request, 'core/profissionais.html')

#
# class Signup(CreateView):
#     model = UserProfile
#     fields = '__all__'

# def signup(request):
#
#     if request.method == 'POST':
#         form1 = UserModelForm(request.POST, instance=request.user)
#         form2 = UserProfModelForm(request.POST)
#
#         if form1.is_valid() and form2.is_valid():
#             user = form1.save()
#             profile = form2.save()
#             form2
#             profile
#             login(request, user)
#             return redirect('home')
#     else:
#         form1 = UserModelForm()
#         form2 = UserProfModelForm()
#         return render(request, 'core/signup.html', {'user_form': form1, 'profile_form': form2})

def signup(request):
    if request.method == 'POST':
        form1 = UserModelForm(request.POST)

        if form1.is_valid():
            user = form1.save()
            login(request, user)
            return redirect('home')
    else:
        form1 = UserModelForm()
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
