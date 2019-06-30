import re
from django.utils import timezone

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.db import models

class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=200)
    razao_social = models.CharField(max_length=200)
    CNPJ = models.CharField(max_length=14)

    def __str__(self):
        return self.nome_fantasia


class TpTelefone(models.Model):
    descricao = models.CharField(null=False, max_length=100)
    sn_ativo = models.BooleanField(default=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    pass


class Telefone(models.Model):
    tp_telefone = models.OneToOneField(TpTelefone, on_delete=models.CASCADE)
    ddd = models.CharField(null=False, max_length=3)
    numero = models.CharField(null=False, max_length=20)

    def __str__(self):
        return self.ddd + '-' + self.numero


class Categoria(models.Model):
    description = models.CharField(max_length=400)
    creation_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True,
                              is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('username'), max_length=15, unique=True, help_text=(
        'Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators=[
        validators.RegexValidator(re.compile('^[\w.@+-]+$'), ('Enter a valid username.'), ('invalid'))])
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    email = models.EmailField(('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(('staff status'), default=False,
                                   help_text=('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(('active'), default=True, help_text=(
        'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(('trusty'), default=False,
                                    help_text=('Designates whether this user has confirmed his account.'))
    dt_nascimento = models.DateField(null=True)
    CPF = models.CharField(max_length=14, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Profissional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    valor_hora = models.CharField(null=True, max_length=10)
    observacao = models.CharField(max_length=400)
    descricao = models.TextField(max_length=2000)
    sn_disponivel_procura = models.BooleanField(default=True)
    sn_consultor = models.BooleanField(default=False)
    sn_ativo = models.BooleanField(default=True)
    foto = models.ImageField(null=True, blank=True, upload_to='galeria/original')