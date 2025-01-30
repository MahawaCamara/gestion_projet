from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from user.forms import LoginForm, RegistrationForm
from .models import Utilisateur
from django.contrib.sessions.models import Session
from django.utils.timezone import now
from django.core.paginator import Paginator
# Vue pour la connexion utilisateur
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)  # Connecte l'utilisateur
                messages.success(request, "Vous êtes maintenant connecté.")
                return redirect('accueil')  # Assurez-vous que 'accueil' correspond à une URL nommée dans votre application
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = LoginForm()
    
    return render(request, 'user/connexion.html', {'form': form})

# # Vue pour la déconnexion utilisateur
# def user_logout(request):
#     logout(request)  # Déconnecte l'utilisateur
#     messages.success(request, "Vous avez été déconnecté.")
#     return redirect('login')  # Assurez-vous que 'connexion' est une URL nommée pour la page de connexion

def utilisateur_auth_toggle(request, pk, action):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)

    if action == "connecter":
        # Connecter l'utilisateur (si ce n'est pas déjà fait)
        if request.user != utilisateur:
            login(request, utilisateur)
            messages.success(request, f"L'utilisateur {utilisateur.nom} a été connecté.")
        else:
            messages.warning(request, f"L'utilisateur {utilisateur.nom} est déjà connecté.")
    elif action == "deconnecter":
        # Déconnecter l'utilisateur (uniquement s'il est déjà connecté)
        if request.user == utilisateur:
            logout(request)
            messages.success(request, f"L'utilisateur {utilisateur.nom} a été déconnecté.")
        else:
            messages.warning(request, f"L'utilisateur {utilisateur.nom} n'est pas connecté.")

    return redirect('user:utilisateur_list')


# Vue pour l'inscription utilisateur
def register(request, pk=None):
    is_edit = pk is not None  # Vérifie si nous modifions ou créons
    utilisateur = get_object_or_404(Utilisateur, pk=pk) if is_edit else None

    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            # Message de succès après la création ou modification
            if is_edit:
                messages.success(request, "L'utilisateur a été modifié avec succès.")
            else:
                messages.success(request, "L'utilisateur a été créé avec succès.")
            return redirect('user:utilisateur_list')
        else:
            # Ajouter un message d'erreur si le formulaire n'est pas valide
            messages.error(request, "Une erreur s'est produite. Veuillez vérifier les champs.")
    else:
        form = RegistrationForm(instance=utilisateur)

    return render(request, 'user/inscription.html', {'form': form, 'is_edit': is_edit})

#Vue pour lister tous les utilsateurs
def utilisateur_list(request):
    # Récupérer tous les utilisateurs
    utilisateurs = Utilisateur.objects.all()
    paginator = Paginator(utilisateurs, 5)  # Affiche 5 utilisateurs par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Récupérer les utilisateurs connectés
    sessions = Session.objects.filter(expire_date__gte=now())
    user_id_list = [session.get_decoded().get('_auth_user_id') for session in sessions]
    utilisateurs_connectes = Utilisateur.objects.filter(id__in=user_id_list)

    return render(request, 'user/utilisateur_list.html', { 
        'page_obj': page_obj, 
        'utilisateurs_connectes': utilisateurs_connectes
    })

# Vue pour afficher les détails d'un utilisateur
def utilisateur_detail(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)
    return render(request, 'user/utilisateur_detail.html', {'utilisateur': utilisateur})

# Vue pour confirmer la suppression d'un utilisateur
def utilisateur_confirm_delete(request, pk):
    # Récupérer l'utilisateur à supprimer
    utilisateur = get_object_or_404(Utilisateur, pk=pk)

    # Supprimer l'utilisateur
    utilisateur.delete()

    # Ajouter un message de succès
    messages.success(request, "L'utilisateur a été supprimé avec succès.")

    # Rediriger vers la liste des utilisateurs
    return redirect('user:utilisateur_list')
