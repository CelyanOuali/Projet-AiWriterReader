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
#from django.conf.urls import url
from aiwriter.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Vos autres vues...
    path('generate-story/', ReactView.as_view(), name='generate_story'),
]




# from django.contrib import admin
# from django.urls import path, include
# #from django.conf.urls import url
# from aiwriter.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', ReactView.as_view(), seas="anything")
# ]

