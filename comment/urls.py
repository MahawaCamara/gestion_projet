from django.urls import path
from . import views

urlpatterns = [
    path('commentaires/', views.list_comment_all, name='list_comment_all'),
    path('tache/<int:tache_pk>/commentaire/ajouter/', views.ajouter_ou_modifier_commentaire, name='ajouter_commentaire'),
    path('tache/<int:tache_pk>/commentaire/<int:commentaire_pk>/modifier/', views.ajouter_ou_modifier_commentaire, name='modifier_commentaire'),
    path('commentaire/<int:id>/', views.detail_commentaire, name='detail_commentaire'),  # Détail du commentaire
    path('tache/<int:tache_pk>/commentaire/supprimer/<int:commentaire_pk>/', views.supprimer_commentaire, name='supprimer_commentaire'),

]
