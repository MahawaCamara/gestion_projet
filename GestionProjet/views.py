from django.shortcuts import render

def error_404_view(request, exception):
    """Vue pour gérer les erreurs 404."""
    return render(request, 'errors/404.html', status=404)
