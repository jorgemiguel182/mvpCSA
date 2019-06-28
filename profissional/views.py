from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from core.models import Profissional
from profissional.forms import CreateModelForm


def index(request):
    return render(request, 'profissional/index.html')

#@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form1 = CreateModelForm(request.POST, request.user)
        print(request.POST)
        if form1.is_valid():
            prof = form1.save(commit=False)
            prof.user = request.user
            prof.observacao = form1.cleaned_data['observacao','']
            print(prof.valor_hora)
            prof.save()

            return render(request, 'profissional/index.html')
    else:
        form1 = CreateModelForm()
        return render(request, 'profissional/create.html', {'user_form': form1})


