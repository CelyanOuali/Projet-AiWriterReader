
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

### gérer la connexion

@api_view(['POST'])
def login(request):
    username = request.data.get('name')
    password = request.data.get('password')

    # Vérifiez les informations d'identification de l'utilisateur
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Authentification réussie, connectez l'utilisateur
        login(request, user)
        return Response({'message': 'Login successful'})
    else:
        # Authentification échouée, renvoyer une réponse d'erreur
        return Response({'message': 'Invalid credentials'}, status=401)