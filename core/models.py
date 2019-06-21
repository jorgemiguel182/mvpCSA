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
