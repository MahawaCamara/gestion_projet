from django import forms
from django.db import models
from GestionProjet import settings
from tache.models import Tâche
from user.models import Utilisateur

# Create your models here.
class Commentary(models.Model): 
    contenu = models.TextField()
    tache = models.ForeignKey('tache.Tâche', on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey('user.Utilisateur', on_delete=models.CASCADE)  # Relation vers Utilisateur
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.tache}"
    



