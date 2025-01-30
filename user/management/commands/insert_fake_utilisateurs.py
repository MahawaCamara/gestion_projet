from django.core.management.base import BaseCommand
from faker import Faker
from user.models import Utilisateur  # Remplacez 'myapp' par le nom de votre application

class Command(BaseCommand):
    help = 'Remplir la base de données avec des utilisateurs fictifs'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Créez 10 utilisateurs fictifs (vous pouvez ajuster ce nombre)
        for _ in range(10):
            # Créez un utilisateur avec des données générées par Faker
            utilisateur = Utilisateur.objects.create(
                email=fake.unique.email(),  # Génère un email unique pour chaque utilisateur
                nom=fake.name(),  # Génère un nom complet
                date_inscription=fake.date_this_decade(),  # Génère une date d'inscription dans cette décennie
            )

            # Affichez un message de succès pour chaque utilisateur créé
            self.stdout.write(self.style.SUCCESS(f'Utilisateur créé: {utilisateur.email}'))
