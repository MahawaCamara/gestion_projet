
import os
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from GestionProjet import settings
from project.forms import ProjectForm
from .models import Project  
from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def list_project(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'project/project_list.html', {'projects': projects ,'page_obj':  page_obj })

# Vue pour afficher les détails d'un projet spécifique
@login_required 
def detail_project(request, pk):
    project = get_object_or_404(Project, pk=pk)  
    return render(request, 'project/detail_project.html', {'project': project})

#vue pour creer un nouveau project
@login_required  # Assure que seul un utilisateur connecté peut accéder à cette vue
def nouveau_project(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('list_project')
        
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.createur = request.user  # Associer l'utilisateur connecté comme créateur
            projet.save()
            messages.success(request, "Le projet a été ajouté avec succès.")
            return redirect('list_project')
    else:
        form = ProjectForm()

    return render(request, 'project/project_form.html', {'form': form})

#vue pour modifier un project existant
@login_required 
def modifier_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    # Vérification si l'utilisateur est le créateur
    if project.createur != request.user:
        messages.error(request, "Vous n'êtes pas autorisé à modifier ce projet.")
        return redirect('list_project')

    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('list_project')

        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Le projet a été modifié avec succès.")
            return redirect('list_project')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'project/project_form.html', {'form': form})

#vue pour supprimer un project existant
@login_required 
def supprimer_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    # Vérification si l'utilisateur est le créateur
    if project.createur != request.user:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer ce projet.")
        return redirect('list_project')

    project.delete()
    messages.success(request, "Le projet a été supprimé avec succès.")
    return redirect('list_project')

# Vue pour la page d'accueil
def home(request):
    projets_recents = Project.objects.all().order_by('-date_creation')[:5]  # Tous les projets
    return render(request, 'project/accueil.html', {'projets_recents': projets_recents})

#vue pour encoyer l'email
def envoyer_email(request):
    if request.method == "POST":
        # Lien GitHub du projet
        github_url = "https://github.com/MahawaCamara/gestion_projet.git"  # Remplacez par votre lien GitHub

        # Envoi de l'email
        subject = "Voici le lien GitHub du projet"
        message = f"Bonjour,\n\nVoici le lien GitHub de mon projet Gestion des projets : {github_url}\n\nCordialement."
        from_email = 'mahawacamaracamara278@gmail.com'  # Votre adresse e-mail
        recipient_list = ['mahawacamaracamara278@gmail.com']  # L'adresse du destinataire

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, "L'e-mail a été envoyé avec succès.")
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite : {str(e)}")
    
    return redirect('accueil')  # Redirigez vers la page principale ou autre page
