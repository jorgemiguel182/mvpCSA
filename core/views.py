from django.shortcuts import render


def home(request):

    return render(request, 'core/home.html')


def profissionais(request):
    return render(request, 'core/profissionais.html')
