from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profissional/', views.profissionais, name='profissionais'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]