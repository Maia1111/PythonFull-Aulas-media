from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [       
    path('cadastro', views.cadastro, name='cadastro' ),
    path('listar', views.listar,  name='listar'),
    path('listar_unico/<int:id>', views.listar_unico, name='listar_unico')
]