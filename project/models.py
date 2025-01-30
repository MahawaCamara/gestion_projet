from django.db import models
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

class Project(models.Model):
    nom = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)  # Pour trier par date
    createur = models.ForeignKey('user.Utilisateur', on_delete=models.CASCADE, related_name='projects')  # L'utilisateur qui a créé le projet
    def __str__(self):
        return self.nom

