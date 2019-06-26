from django.shortcuts import render, redirect

from profissional.forms import CreateModelForm


def index(request):
    return render(request, 'profissional/index.html')

def create(request):
    if request.method == 'POST':
        form1 = CreateModelForm(request.POST)

        if form1.is_valid():
            form1.save()
            return render(request, 'profissional/index.html')
    else:
        form1 = CreateModelForm()
        return render(request, 'profissional/create.html', {'user_form': form1})