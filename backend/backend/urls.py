#urls.py

"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, seas='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), seas='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
#router: permet de faire les requêtes: /stories/ (liste de tous les objets de la classe React - Methodes CREATE et READ) , 
# /stories/id (renvoie un seul objet de la classe React via id, une pk, - Méthodes UPDATE et DELETE)  
from rest_framework import routers
from aiwriter import views
from aiwriter.api.signin import signup
from aiwriter.api.login import login
#from aiwriter.api.views import signup

router = routers.DefaultRouter()

#/api/stories : lien django Api Root
#enregistrer la vue StoryView de l'app aiwriter avec 
#le nom aiwriter pour l'URL api/stories/
#création automatique des routes nécessaires pour les opérations 
# CRUD (Create, Read, Update, Delete) sur les histoires.
router.register(r'stories', views.StoryView, 'aiwriter')

urlpatterns = [
    #interface administration (gestions des utilisateurs, des groupes, des modèles de base de données)
    path('admin/', admin.site.urls),
    #url racine, qui donne accès à la collection de toutes les histoires, via http://127.0.0.1:8000/api/stories/
    path('api/', include(router.urls)),
    #url API, endpoint inscription
    path('api/signup/', signup, name='signup'),
    #url API, endpoint connexion
    path('api/login/', login, name='login'),
]


