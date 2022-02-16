"""CoachingDrills URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blog.views import signup, profile, exercise_add, logout_view
from django.contrib.auth import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('compte/nouveau', signup, name='signup'),
    # path('compte/', include('django.contrib.auth.urls')),
    path('compte/connexion', views.LoginView.as_view(), name='login'),
    path('compte/deconnexion', logout_view, name="logout"),
    path('accounts/profile/', profile, name="profile page"),
    path('exercice/ajouter', exercise_add, name="adding an exercise")
]

import django.contrib.auth.urls