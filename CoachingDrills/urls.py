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
from blog.views import index, signup, profile, exercise_add, logout_view, exercices_listing, tags_listing, categories_listing, category_add, tag_add, exercise_delete, category_delete, tag_delete, exercise_detail, category_detail, tag_detail, exercise_edit, tag_edit, category_edit
from django.contrib.auth import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', index, name='index'),

    # creation
    path('admin/exercices/ajouter', exercise_add, name="adding exercise"),
    path('admin/categories/ajouter', category_add, name="adding category"),
    path('admin/tags/ajouter', tag_add, name="adding tag"),

    #listing
    path('admin/exercises', exercices_listing, name='exercise_listing'),
    path('admin/categories', categories_listing, name='category_listing'),
    path('admin/tags', tags_listing, name='tag_listing'),

    # detail
    path('admin/exercise/<int:pk>/detail', exercise_detail, name='exercise detail'),
    path('admin/category/<int:pk>/detail', category_detail, name='category detail'),
    path('admin/tag/<int:pk>/detail', tag_detail, name='tag detail'),

    # edit
    path('admin/exercise/<int:pk>/edit', exercise_edit, name="edit exercise"),
    path('admin/category/<int:pk>/edit', category_edit, name="edit category"),
    path('admin/tag/<int:pk>/edit', tag_edit, name="edit tag"),


    # deletion
    path("admin/exercise/<int:pk>/delete", exercise_delete, name="delete exercise"),
    path('admin/category/<int:pk>/delete', category_delete, name="delete category"),
    path('admin/tag/<int:pk>/delete', tag_delete, name="delete tag"),


    # authentification 
    path('compte/nouveau', signup, name='signup'),
    # path('compte/', include('django.contrib.auth.urls')),
    path('compte/connexion', views.LoginView.as_view(), name='login'),
    path('compte/deconnexion', logout_view, name="logout"),
    path('accounts/profile/', profile, name="profile page"),

   
]
