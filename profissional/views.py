from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from core.models import Profissional, Categoria
from profissional.forms import CreateProfissionalForm


class Index(ListView):
    model = Profissional
    paginate_by = 15


    def def_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profissional'] = Profissional.objects.get(user=super.user).exists()
        return context


@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = CreateProfissionalForm(request.POST, request.FILES)
        #        print(form.cleaned_data)
        print(form)
        print(request.user)
        print(form.is_valid())
        if form.is_valid():
            user = request.user
            categoria = request.POST['categoria']
            print(categoria)
            valor_hora = form.cleaned_data['valor_hora']
            observacao = form.cleaned_data['observacao']
            descricao = form.cleaned_data['descricao']
            sn_disponivel_procura = form.cleaned_data['sn_disponivel_procura']
            sn_consultor = form.cleaned_data['sn_consultor']
            sn_ativo = form.cleaned_data['sn_ativo']
            foto = form.cleaned_data['foto']

            categoria = Categoria.objects.get(id__exact=categoria)

            print(categoria)
            Profissional(user=user, categoria=categoria, valor_hora=valor_hora, observacao=observacao,
                                descricao=descricao,
                                sn_disponivel_procura=sn_disponivel_procura, sn_consultor=sn_consultor,
                                sn_ativo=sn_ativo, foto=foto).save()


            print(form.cleaned_data)

            return redirect('/profissional/')
    else:
        form = CreateProfissionalForm();
        return render(request, 'profissional/create.html', {'user_form': form})

# @login_required
# def create(request):
#     if request.method == 'POST':
#         form1 = CreateModelForm(request.POST, request.user)
#
#         if form1.is_valid():
#           #  user = request.user.id
#             prof = form1.save(commit=False)
#             prof.user = request.user
#             print(prof.categoria)
#             print(prof.valor_hora)
#             print(prof)
#             prof.save()
# #        print(form1.cleaned_data['categoria'])
#  #       post_categoria = form1.cleaned_data['categoria']
#       #  post_categoria = 1
#       #   post_valor_hora = form1.cleaned_data['valor_hora']
#       #   post_observacao = form1.cleaned_data['observacao']
#       #   post_descricao = form1.cleaned_data['descricao']
#       #   post_sn_disponivel_procura = form1.cleaned_data['sn_disponivel_procura']
#       #   post_sn_consultor = form1.cleaned_data['sn_consultor']
#       #   post_sn_ativo = form1.cleaned_data['sn_ativo']
#       #   post_foto = form1.cleaned_data['foto']
#
#         # Profissional(user, post_categoria, post_valor_hora, post_observacao, post_descricao,
#         #              post_sn_disponivel_procura, post_sn_consultor, post_sn_ativo, post_foto)
#
#             return render(request, 'profissional/index.html')
#     else:
#         form1 = CreateModelForm()
#         return render(request, 'profissional/create.html', {'user_form': form1})
