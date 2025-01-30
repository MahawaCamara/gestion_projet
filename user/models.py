from django.utils import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Crée et retourne un utilisateur avec un email et un mot de passe.
        """
        if not email:
           raise ValueError("L'adresse e-mail doit être fournie")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crée et retourne un superutilisateur avec un email et un mot de passe.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    date_inscription = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Redéfinir les relations pour éviter les conflits
    groups = models.ManyToManyField(
    'auth.Group',
    related_name='utilisateurs_groups', # Nom unique pour la relatio inverse
    blank=True
    )
    user_permissions = models.ManyToManyField(
    'auth.Permission',
    related_name='utilisateurs_permissions', # Nom unique pour la relation inverse
    blank=True
    )
    objects = UtilisateurManager()
    USERNAME_FIELD = 'email' # Utilisation de l'email comme identifiant
    REQUIRED_FIELDS = ['nom'] # Autres champs requis lors de la
    # création d'un utilisateur
    def __str__(self):
      return self.email