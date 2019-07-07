from django import forms
from core.models import Categoria

class CreateProfissionalForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset = Categoria.objects.all(), help_text="Selecione uma categoria")
    valor_hora = forms.FloatField()
    observacao = forms.CharField(max_length=300, empty_value="Título")
    descricao = forms.CharField(max_length="2000", empty_value="Conte um pouco mais sobre você!")
    sn_consultor = forms.BooleanField(label="Você é um consultor ?", initial=False, required=False)
    sn_disponivel_procura = forms.BooleanField(label="Ficar visível para as empresas ?", initial=True, required=False)
    sn_ativo = forms.BooleanField(label="Cadastro ativo.", initial=True, required=False)
    foto = forms.ImageField(label="Foto de perfil", required=False)

