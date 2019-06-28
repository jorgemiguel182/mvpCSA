from django import forms
from django.forms import Select

from core.models import Profissional, Categoria


class CreateModelForm(forms.ModelForm):
    #categoria = Categoria.objects
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), to_field_name='id', widget=Select(attrs={'style':'background_color:#F5F8EC'}))

    class Meta:
        model = Profissional
        fields = ['categoria', 'valor_hora', 'observacao', 'descricao', 'sn_disponivel_procura', 'sn_consultor', 'sn_ativo', 'foto',]
