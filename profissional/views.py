from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from core.models import Profissional, Categoria
from profissional.forms import CreateProfissionalForm

@login_required(login_url='/login/')
class Index(ListView):
    model = Profissional
    paginate_by = 15


    def def_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profissional'] = Profissional.objects.get(user=super.user).exists()
        return context


@login_required(login_url='/login/')
def index(request):
    profissionais = Profissional.objects.all()
    form = CreateProfissionalForm()
    return render(request, 'profissional/profissional_list.html', {'profissionais' : profissionais, 'form': form})


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

            return redirect('/profissional/profissional_list.html')
    else:
        form = CreateProfissionalForm();
        return render(request, 'profissional/create.html', {'user_form': form})