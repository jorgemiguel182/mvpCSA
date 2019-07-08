from django.urls import path
from profissional import views

app_name="profissional"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/detalhe/', views.detalhe, name="detalhe"),
    path('<int:pk>/edit/', views.edit, name="edit"),
]
