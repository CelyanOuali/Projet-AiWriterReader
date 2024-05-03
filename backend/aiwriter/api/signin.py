


from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response



#### gérer l'inscription...
@api_view(['POST'])
def signup(request):
    username = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    # Créez un nouvel utilisateur dans la base de données
    user = User.objects.create_user(username=username, email=email, password=password)

    return Response({'message': 'User created successfully'})



