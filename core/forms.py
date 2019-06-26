from django import forms
#from django.contrib.auth.models import User

from core.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


# class UserModelForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'email']
#

class UserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'CPF', 'dt_nascimento']





# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = UserProfile
#         fields = ('CPF',)


class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    dt_nascimento = forms.DateField()
    CPF = forms.CharField(max_length=100)
    #user = forms.ModelMultipleChoiceField(queryset=User.objects.all())