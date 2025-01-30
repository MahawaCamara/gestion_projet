from django import forms
from .models import Commentary
class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['contenu']  
        widgets = {
            'contenu' : forms.Textarea(attrs={
                'class': 'form-control custom-description fs-6',
                'rows' : 2,
                'style': 'resize: vertical',
                'placeholder' : 'Entrer le contenu du commentaire',
                'required': True,
            }),
        }