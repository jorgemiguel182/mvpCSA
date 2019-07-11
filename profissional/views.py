from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Profissional, Categoria
from profissional.forms import CreateProfissionalForm, EditProfissionalForm


def Is_prof(user):
    is_prof = None
    try:
        is_prof = Profissional.objects.get(user=user)
    except Profissional.DoesNotExist:
        is_prof = None
    return is_prof

@login_required(login_url='/login/')
def index(request):
    is_prof = Is_prof(request.user)
   # print(is_prof.pk)

    ##FILTER
    categoria = Categoria.objects.all()
    qs = Profissional.objects.all()
    categoriaSearch = request.GET.get('categoriaSearch')

    if categoriaSearch != '' and categoriaSearch is not None:
        categoria = categoria.filter(description__icontains=categoriaSearch)
        qs = qs.filter(categoria__in=categoria)
    ##ENDFILTER

    profissionais = Profissional.objects.all()
    return render(request, 'profissional/profissional_list.html',  {'queryset':qs, 'profissionais' : profissionais, 'is_prof': is_prof})

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

@login_required(login_url='/login/')
def detalhe(request, pk):
    prof = get_object_or_404(Profissional, pk=pk)
    is_prof = Is_prof(request.user)
    print(is_prof, is_prof.pk, pk)
    if request.method == 'POST':
        pass

    return render(request, 'profissional/prof_prof_detalhes.html', {'prof': prof, 'is_prof': is_prof})

@login_required(login_url='/login/')
def edit(request, pk):
    is_prof = Is_prof(request.user)
    prof = get_object_or_404(Profissional, pk=pk)
    if request.method == "POST":
        form = EditProfissionalForm(request.POST, instance=prof)
        if form.is_valid():
            prof = form.save()
            return redirect('/profissional/index',  {'is_prof': is_prof})
    else:
        form = EditProfissionalForm(instance=prof)
    return render(request, 'profissional/user_prof_detalhes.html', {'form': form, 'is_prof': is_prof})