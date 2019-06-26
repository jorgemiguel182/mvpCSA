from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#from core.forms import CustomUserCreationForm


from .models import Empresa, Categoria, TpTelefone, Telefone, Profissional
from .models import User

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(TpTelefone)
admin.site.register(Telefone)
admin.site.register(Profissional)
admin.site.register(User)

#class CustomUserAdmin(UserAdmin):
##    add_form = CustomUserCreationForm
 #   model = User
 #   list_display = ['email', 'username', 'CPF']