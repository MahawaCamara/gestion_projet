# urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'), # Inscription
    path('register/<int:pk>/', views.register, name='edit_user'), # Modification
    path('login/', LoginView.as_view(template_name='user/connexion.html'), name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('utilisateur/<int:pk>/auth/<str:action>/', views.utilisateur_auth_toggle, name='utilisateur_auth_toggle'),
    path('list', views. utilisateur_list, name='utilisateur_list'),
    path('utilisateur/<int:pk>/', views.utilisateur_detail, name='utilisateur_detail'),
     path('utilisateur/<int:pk>/supprimer/', views.utilisateur_confirm_delete, name='utilisateur_confirm_delete'),  # Changement ici
]