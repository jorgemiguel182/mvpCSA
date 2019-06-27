from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.models import Profissional
from profissional.forms import CreateModelForm


def index(request):
    return render(request, 'profissional/index.html')

@login_required
def create(request):
    if request.method == 'POST':
        form1 = CreateModelForm(request.user, request.POST)

        if form1.is_valid():
          #  user = request.user.id
            prof = form1.save(commit=False)
            prof.user = request.user
            print(prof.categoria)
            print(prof)
            prof.save()
#        print(form1.cleaned_data['categoria'])
 #       post_categoria = form1.cleaned_data['categoria']
      #  post_categoria = 1
      #   post_valor_hora = form1.cleaned_data['valor_hora']
      #   post_observacao = form1.cleaned_data['observacao']
      #   post_descricao = form1.cleaned_data['descricao']
      #   post_sn_disponivel_procura = form1.cleaned_data['sn_disponivel_procura']
      #   post_sn_consultor = form1.cleaned_data['sn_consultor']
      #   post_sn_ativo = form1.cleaned_data['sn_ativo']
      #   post_foto = form1.cleaned_data['foto']

        # Profissional(user, post_categoria, post_valor_hora, post_observacao, post_descricao,
        #              post_sn_disponivel_procura, post_sn_consultor, post_sn_ativo, post_foto)

            return render(request, 'profissional/index.html')
    else:
        form1 = CreateModelForm()
        return render(request, 'profissional/create.html', {'user_form': form1})
