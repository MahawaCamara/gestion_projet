from django.urls import path
from project import views

urlpatterns = [
    path('', views.home, name='accueil'),
    path('projet/', views.list_project, name='list_project'),
    path('projet/<int:pk>/', views.detail_project, name='detail_project'),
    path('nouveau_project/', views.nouveau_project, name='nouveau_project'),
    path('modifier_project/<int:pk>/', views.modifier_project, name='modifier_project'),
    path('supprimer_project/<int:pk>/', views.supprimer_project, name='supprimer_project'),
    # D'envoi d'email
    path('envoyer_email/', views.envoyer_email, name='envoyer_email')

]
