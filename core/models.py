from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    description = models.CharField(max_length=400)
    creation_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.description

class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=200)
    razao_social = models.CharField(max_length=200)
    CNPJ = models.CharField(max_length=14)

    def __str__(self):
        return self.nome_fantasia

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(null=False, max_length=200)
    dt_nascimento = models.DateField(null=False)
    email = models.EmailField(null=False)
    CPF = models.CharField(max_length=14, null=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class TpTelefone(models.Model):
    descricao = models.CharField(null=False, max_length=100)
    sn_ativo = models.BooleanField(default=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

class Telefone(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    tp_telefone = models.OneToOneField(TpTelefone, on_delete=models.CASCADE)
    numero = models.CharField(null=False, max_length=20)
    ddd = models.CharField(null=False, max_length=3)

    def __str__(self):
        return self.ddd + '-' + self.numero