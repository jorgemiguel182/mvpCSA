from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TestForm

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
