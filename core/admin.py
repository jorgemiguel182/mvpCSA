from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.forms import CustomUserCreationForm
from .models import Empresa, Categoria, User, TpTelefone, Telefone

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(User,UserAdmin)
admin.site.register(TpTelefone)
admin.site.register(Telefone)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    list_display = ['email', 'username','CPF']