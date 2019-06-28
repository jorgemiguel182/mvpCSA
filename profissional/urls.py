from django.urls import path
from profissional import views
app_name="profissional"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
]