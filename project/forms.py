from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
   class Meta:
        model = Project
        fields = ['nom', 'description', 'image'] 
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control fs-4',
                'placeholder': 'Nom du projet',
                'required': True,
                'style': 'padding: 10px;',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control description-field fs-4',
                'placeholder': 'Description du projet...',
                'rows': 2,
                'required': True,
                'style': 'padding: 10px; margin-top: 20px;',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control fs-4',   
            }),
        }
        labels = {
            'nom': '',
            'description': '',
            'image': 'Image du projet',  
        }
