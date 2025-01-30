
from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_tache, name='list_tache'),
    path('tache/<int:pk>/', views.detail_tache, name='detail_tache'),
    path('nouvelle_tache/', views.nouvelle_tache, name='nouvelle_tache'), 
    path('modifier_tache/<int:pk>', views.modifier_tache, name='modifier_tache'), 
    path('supprimer_tache/<int:pk>/', views.supprimer_tache, name='supprimer_tache'), 
]
