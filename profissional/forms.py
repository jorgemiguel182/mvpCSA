from django import forms

from core.models import Profissional


class CreateModelForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['categoria', 'valor_hora', 'observacao', 'descricao', 'sn_disponivel_procura', 'sn_consultor', 'sn_ativo','foto']

