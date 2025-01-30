# Projet Django

Ce projet est une application web développée avec Django.
Ce site consiste a faire la gestion des projets s'ocupe à la creation des projets et chaque projet a un nom et une description . L'utilisateur n'a le droit d'ajouter un projet si et seulement s'il est authentifié. Et seulement le crateur du projet n'a le droit de modifié ou supprimé le projet.

Parlant de la tache  veuillez consulter le model tâche pour voir son fonctionnement et ella a la même logique qu'au projet . Pour creer une tâche il faut d'abord être authentifié aisi de suite comme pour le projet.

Commentaire même logique.

Utilisateur un administeur est creer par default qui admin@gmail.com et le mot de pass est admin1234@ vous pouvez vous connecter pour tester les logiques que je vienne d'énumerer.

Une page d'accueille qui nous s'affiche les images des projets recemment creer .



## Installation

1. Clonez le repository :
    ```bash
    git clone https://github.com/MahawaCamara/gestion_projet.git
    ```
2. Créez un environnement virtuel :
    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows : env\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations :
    ```bash
    python manage.py migrate
    ```

5. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

## Envoi d'e-mails

L'application utilise un serveur SMTP pour envoyer des e-mails. Vous pouvez configurer les paramètres de votre serveur dans `settings.py`.

## Auteur

- Mahawa Camara Programmeure en developpement web licence 4 à Barack Obama
