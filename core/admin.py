from django.contrib import admin
from .models import Empresa, Categoria, UserProfile, TpTelefone, Telefone

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(UserProfile)
admin.site.register(TpTelefone)
admin.site.register(Telefone)