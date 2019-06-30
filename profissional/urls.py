from django.urls import path
from profissional import views
from profissional.views import Index

app_name="profissional"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create, name="create"),
]