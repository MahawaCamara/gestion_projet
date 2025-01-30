from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from tache.models import Tâche
from .models import Commentary
from .forms import CommentaryForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def list_comment_all(request):
    commentaires = Commentary.objects.all()  # Récupère tous les commentaires
    paginator = Paginator(commentaires, 5)  # 10 commentaires par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'comment/list_commentaire.html', {'page_obj': page_obj})


@login_required
def ajouter_ou_modifier_commentaire(request, tache_pk, commentaire_pk=None):
    tache = get_object_or_404(Tâche, pk=tache_pk)

    # Si commentaire_pk est fourni, récupérez le commentaire ; sinon, créez un nouveau
    if commentaire_pk:
        commentaire = get_object_or_404(Commentary, pk=commentaire_pk, tache=tache)
        # Vérifiez que seul l'auteur peut modifier
        if commentaire.auteur != request.user:
            messages.error(request, "Vous n'êtes pas autorisé à modifier ce commentaire.")
            return redirect('list_comment_all')
    else:
        commentaire = Commentary(tache=tache)

    if request.method == 'POST':
        form = CommentaryForm(request.POST, instance=commentaire)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user  # Associez l'auteur comme l'utilisateur connecté
            commentaire.save()
            
            # Condition pour rediriger selon le contexte
            if commentaire_pk:  # Modification
                messages.success(request, "Le commentaire a été modifié avec succès.")
                return redirect('list_comment_all')  # Redirection vers la liste des commentaires
            else:  # Ajout
                messages.success(request, "Le commentaire a été ajouté avec succès.")
                return redirect('detail_tache', pk=tache.pk)  # Redirection vers le détail de la tâche
    else:
        form = CommentaryForm(instance=commentaire)

    return render(request, 'comment/ajouter_commentaire.html', {
        'form': form,
        'tache': tache,
        'commentaire': commentaire if commentaire_pk else None,
    })

@login_required
def detail_commentaire(request, id):
    commentaire = get_object_or_404(Commentary, id=id)
    return render(request, 'comment/detail_commentaire.html', {'commentaire': commentaire})

@login_required
def supprimer_commentaire(request, tache_pk, commentaire_pk):
    commentaire = get_object_or_404(Commentary, pk=commentaire_pk, tache_id=tache_pk)
    if commentaire.auteur != request.user:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer ce commentaire.")
        return redirect('list_comment_all')

    commentaire.delete()
    messages.success(request, "Commentaire supprimé avec succès.")
    return redirect('list_comment_all')

