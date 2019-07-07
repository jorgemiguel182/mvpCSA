from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.html import format_html

from core.models import User
from django.contrib.auth.forms import UserCreationForm

# class UserModelForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'CPF', 'dt_nascimento' ]

class UserModelForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'CPF', 'dt_nascimento' ]

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError('Please enter your email address.')
        if User.objects.filter(email__iexact=email).exists():
            message = format_html(
                'User with this Email account already exists.Please click <a href="{}">here</a> if you forgot your password',
                reverse('account_forgot_password'))
            raise ValidationError(message)
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    # def clean_confirm_email(self):
    #     confirm_email = self.cleaned_data['confirm_email']
    #     if 'email' in self.cleaned_data and self.cleaned_data['email'] != confirm_email:
    #         raise forms.ValidationError("Emails do not match.")
    #     return confirm_email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
            raise ValidationError('Please enter your first name.')
        return first_name

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if 'password' in self.cleaned_data and self.cleaned_data['password'] != password1:
            raise forms.ValidationError("Passwords do not match.")
        return password1