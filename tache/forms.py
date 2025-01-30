from django import forms
from .models import Tâche

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tâche
        fields = ['titre', 'description', 'projet', 'assigné_a']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control custom-titre',  # Ajoute une classe CSS personnalisée
                'placeholder': 'Entrez le titre de la tâche',
                'style': 'font-size: 1.2em;',  # Taille de la police personnalisée
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control custom-description',  # Classe CSS personnalisée
                'placeholder': 'Entrez la description de la tâche...',
                'rows': 2,  # Nombre de lignes du textarea
                'style': 'resize: vertical;',  # Permet de redimensionner verticalement
                'style': 'margin-top: 20px;',
                'required': True,
            }),
            'projet': forms.Select(attrs={
                'class': 'form-select custom-select',
                'style': 'border-color: #007bff;',  # Couleur de bordure personnalisée
                'style': 'margin-top: 20px;',
                'required': True,
            }),
            'assigné_a': forms.SelectMultiple(attrs={  # Utiliser SelectMultiple ici
                'class': 'form-select custom-select',
                'style': 'border-color: #28a745; margin-top: 20px;',
                'style': 'margin-top: 20px;',
                'required': True,
            }),
            
        }
        
        labels = {
            'titre': '',  # Supprime le label pour le champ "nom"
            'description': '',  # Supprime le label pour le champ "description"
            'Projet': 'Projet',
            'assigné_a': 'assigné_a',
        }
