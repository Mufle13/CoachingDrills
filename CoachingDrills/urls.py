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
from blog.views import index, signup, profile, exercise_add, logout_view, exercices_listing, tags_listing, categories_listing, category_add, tag_add
from django.contrib.auth import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', index, name='index'),
    path('admin/exercices', exercices_listing, name='exercice_listing'),
    path('admin/categories', categories_listing, name='category_listing'),
    path('admin/tags', tags_listing, name='tag_listing'),
    path('compte/nouveau', signup, name='signup'),
    # path('compte/', include('django.contrib.auth.urls')),
    path('compte/connexion', views.LoginView.as_view(), name='login'),
    path('compte/deconnexion', logout_view, name="logout"),
    path('accounts/profile/', profile, name="profile page"),

    path('admin/exercices/ajouter', exercise_add, name="adding an exercise"),
    path('admin/categories/ajouter', category_add, name="adding a category"),
    path('admin/tags/ajouter', tag_add, name="adding a tag")
]

import django.contrib.auth.urls