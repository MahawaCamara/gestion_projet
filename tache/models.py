from django.db import models

class Tâche(models.Model): 
    titre = models.CharField(max_length=255) 
    description = models.TextField() 
    projet = models.ForeignKey('project.Project', on_delete=models.CASCADE)  # Référence en chaîne
    assigné_a = models.ManyToManyField('user.Utilisateur')  # Référence en chaîne
    date_creation = models.DateTimeField(auto_now_add=True)
    createur = models.ForeignKey('user.Utilisateur', on_delete=models.CASCADE, related_name="taches") 
    def __str__(self):
        return self.titre
