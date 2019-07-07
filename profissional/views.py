from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.models import Profissional, Categoria
from profissional.forms import CreateProfissionalForm

@login_required(login_url='/login/')
def index(request):
    print(request.user)
    try:
        is_prof = Profissional.objects.get(user = request.user)
    except Profissional.DoesNotExist:
        is_prof = None

    profissionais = Profissional.objects.all()
    form = CreateProfissionalForm()
    return render(request, 'profissional/profissional_list.html', {'profissionais' : profissionais, 'form': form, 'is_prof': is_prof})


@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = CreateProfissionalForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            categoria = request.POST['categoria']
            valor_hora = form.cleaned_data['valor_hora']
            observacao = form.cleaned_data['observacao']
            descricao = form.cleaned_data['descricao']
            sn_disponivel_procura = form.cleaned_data['sn_disponivel_procura']
            sn_consultor = form.cleaned_data['sn_consultor']
            sn_ativo = form.cleaned_data['sn_ativo']
            foto = form.cleaned_data['foto']

            categoria = Categoria.objects.get(id__exact=categoria)

            Profissional(user=user, categoria=categoria, valor_hora=valor_hora, observacao=observacao,
                                descricao=descricao,
                                sn_disponivel_procura=sn_disponivel_procura, sn_consultor=sn_consultor,
                                sn_ativo=sn_ativo, foto=foto).save()

            return redirect('profissional:index')
    else:
        form = CreateProfissionalForm();
        return render(request, 'profissional/create.html', {'user_form': form})

def detalhe(request):
    return render(request, 'profissional/prof_prof_detalhes.html')