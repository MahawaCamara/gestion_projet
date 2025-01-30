from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from comment.models import Commentary
from tache.forms import TacheForm
from tache.models import Tâche
from django.contrib.auth.decorators import login_required

# Create your views here.

#Vue pour afficher la liste des tâches
def list_tache(request):
    taches = Tâche.objects.order_by()  # Exemple de tri par date de création
    paginator = Paginator(taches, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tache/tache_list.html', {'page_obj': page_obj})


#Vue pour afficher les details d'une tâche
@login_required
def detail_tache(request, pk):
    tache = get_object_or_404(Tâche, pk=pk)
    # Si vous avez défini related_name='commentaires'
    commentaires = tache.commentaires.all()  
    # Sinon, utilisez tache.commentary_set.all()
    # commentaires = tache.commentary_set.all()

    return render(request, 'tache/tache_detail.html', {
        'tache': tache,
        'commentaires': commentaires,
    })


@login_required
def nouvelle_tache(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('list_tache')
        
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.createur = request.user  # Associer l'utilisateur connecté
            tache.save()
            messages.success(request, "La tâche a été ajoutée avec succès.")
            return redirect('list_tache')
        else:
            messages.error(request, "Une erreur est survenue. Veuillez vérifier les champs.")
    else:
        form = TacheForm()
    
    return render(request, 'tache/tache_form.html', {'form': form})

#vue pour modifier une tâche existante
@login_required
def modifier_tache(request, pk):
    tache = get_object_or_404(Tâche, pk=pk)

    # Vérifie si l'utilisateur est le créateur de la tâche ou un super utilisateur
    if request.user != tache.createur and not request.user.is_superuser:
        messages.error(request, "Vous n'avez pas l'autorisation de modifier cette tâche.")
        return redirect('list_tache')

    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('list_tache')
        
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            messages.success(request, "La tâche a été modifiée avec succès.")
            return redirect('list_tache')
        else:
            messages.error(request, "Une erreur est survenue. Veuillez vérifier les champs.")
    else:
        form = TacheForm(instance=tache)
    
    return render(request, 'tache/tache_form.html', {'form': form})

#vue pour supprimer une tâche existante
@login_required
def supprimer_tache(request, pk):
    tache = get_object_or_404(Tâche, pk=pk)
    # Vérifie si l'utilisateur a les droits nécessaires
    if request.user != tache.createur and not request.user.is_superuser:
        messages.error(request, "Vous n'avez pas l'autorisation de supprimer cette tâche.")
        return redirect('list_tache')
    tache.delete()
    messages.success(request, "La tâche a été supprimée avec succès.")
    return redirect('list_tache')

