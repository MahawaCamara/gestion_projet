from django.core.management.base import BaseCommand
from faker import Faker
from comment.models import Commentaire, Tâche, Utilisateur  # Assurez-vous d'importer vos modèles

class Command(BaseCommand):
    help = 'Remplir la base de données avec des commentaires fictifs'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Récupérer toutes les tâches et utilisateurs existants
        tâches = Tâche.objects.all()
        utilisateurs = Utilisateur.objects.all()

        # Vérifier s'il existe des tâches et des utilisateurs pour éviter les erreurs
        if not tâches.exists():
            self.stdout.write(self.style.ERROR("Il n'y a pas de tâches disponibles."))
            return
        if not utilisateurs.exists():
            self.stdout.write(self.style.ERROR("Il n'y a pas d'utilisateurs disponibles."))
            return

        # Créer 10 commentaires fictifs (vous pouvez ajuster ce nombre)
        for _ in range(20):
            # Sélectionner une tâche et un utilisateur aléatoires
            tâche = fake.random_element(tâches)  # Choisir une tâche aléatoire
            utilisateur = fake.random_element(utilisateurs)  # Choisir un utilisateur aléatoire

            # Créer un commentaire avec un contenu généré par Faker
            commentaire = Commentaire.objects.create(
                contenu=fake.text(),  # Génère un contenu de commentaire fictif
                tâche=tâche,  # Associer le commentaire à une tâche
                utilisateur=utilisateur,  # Associer le commentaire à un utilisateur
            )

            # Afficher un message de succès dans la console
            self.stdout.write(self.style.SUCCESS(f'Commentaire créé: "{commentaire.contenu[:50]}..."'))
