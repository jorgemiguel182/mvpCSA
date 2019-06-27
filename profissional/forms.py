from django import forms

from core.models import Profissional, Categoria


class CreateModelForm(forms.ModelForm):
    #categoria = Categoria.objects
    #field1 = forms.ModelChoiceField(queryset=categoria, empty_label=None)

    class Meta:
        model = Profissional
        fields = ['categoria', 'valor_hora', 'observacao', 'descricao', 'sn_disponivel_procura', 'sn_consultor', 'sn_ativo','foto']

    #def __init__(self, *args, **kwargs):
    #    super(CreateModelForm, self).__init__(*args, **kwargs)
    #    self.fields['categoria'].queryset = Categoria.objects