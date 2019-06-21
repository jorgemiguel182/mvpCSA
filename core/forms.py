from django import forms

class TestForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)