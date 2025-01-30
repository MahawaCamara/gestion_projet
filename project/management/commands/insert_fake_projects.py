# myapp/management/commands/populate_projects.py
from django.core.management.base import BaseCommand
from faker import Faker
from project.models import Project
import random

class Command(BaseCommand):
    help = 'Peuple la base de données avec des projets fictifs'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Nombre de projets à créer
        num_projects = 10

        for _ in range(num_projects):
            project_name = fake.company()
            description = fake.text()
            image_name = random.choice(['projet-1.jpg', 'projet-2.jpg', 'projet-3.jpg', 'projet-4.jpg', 'projet.jpg'])

            # Créer un projet
            Project.objects.create(nom=project_name, description=description, image_name=image_name)

        self.stdout.write(self.style.SUCCESS(f'{num_projects} projets ont été créés avec succès!'))
