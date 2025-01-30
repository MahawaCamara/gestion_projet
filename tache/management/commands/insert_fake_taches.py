from django.core.management.base import BaseCommand
from faker import Faker
from tache.models import Tâche, Project, Utilisateur  # Assurez-vous d'importer vos modèles

class Command(BaseCommand):
    help = 'Remplir la base de données avec des tâches fictives'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Récupérer tous les projets et utilisateurs existants
        projets = Project.objects.all()
        utilisateurs = list(Utilisateur.objects.all())  # Convertir le queryset en liste

        # Vérifier s'il existe des projets et des utilisateurs
        if not projets.exists():
            self.stdout.write(self.style.ERROR("Il n'y a pas de projets disponibles."))
            return
        if not utilisateurs:
            self.stdout.write(self.style.ERROR("Il n'y a pas d'utilisateurs disponibles."))
            return

        # Créer 10 tâches fictives (vous pouvez ajuster ce nombre)
        for _ in range(20):
            # Sélectionner un projet et plusieurs utilisateurs aléatoires
            projet = fake.random_element(projets)  # Choisir un projet aléatoire
            assignés = fake.random_elements(utilisateurs, unique=True, length=fake.random_int(min=1, max=5))  # Assigner entre 1 et 5 utilisateurs aléatoires

            # Créer une tâche avec un titre et une description générés par Faker
            tâche = Tâche.objects.create(
                titre=fake.sentence(nb_words=6),  # Génère un titre de tâche
                description=fake.text(),  # Génère une description de tâche
                projet=projet,  # Associer la tâche à un projet
            )

            # Assigner les utilisateurs à la tâche
            tâche.assigné_a.set(assignés)  # Associer les utilisateurs à la tâche via la relation ManyToMany

            # Afficher un message de succès dans la console
            self.stdout.write(self.style.SUCCESS(f'Tâche créée: "{tâche.titre}"'))
