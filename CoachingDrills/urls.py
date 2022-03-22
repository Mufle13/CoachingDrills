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
from blog.views import admin_index, signup, profile, exercise_add, logout_view, exercices_listing, tags_listing, categories_listing, category_add, tag_add, exercise_delete, category_delete, tag_delete, exercise_detail, category_detail, tag_detail, exercise_edit, tag_edit, category_edit, index, exercise_builder, About, ExerciseListing
from django.contrib.auth import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin_index, name='admin'),

    # creation
    path('admin/exercices/ajouter', exercise_add, name="adding_exercise"),
    path('admin/categories/ajouter', category_add, name="adding_category"),
    path('admin/tags/ajouter', tag_add, name="adding_tag"),

    #listing
    path('admin/exercises', exercices_listing, name='exercise_listing'),
    path('admin/categories', categories_listing, name='category_listing'),
    path('admin/tags', tags_listing, name='tag_listing'),

    # detail
    path('admin/exercise/<int:pk>/detail', exercise_detail, name='exercise_detail'),
    path('admin/category/<int:pk>/detail', category_detail, name='category_detail'),
    path('admin/tag/<int:pk>/detail', tag_detail, name='tag_detail'),

    # edit
    path('admin/exercise/<int:pk>/edit', exercise_edit, name="edit_exercise"),
    path('admin/category/<int:pk>/edit', category_edit, name="edit_category"),
    path('admin/tag/<int:pk>/edit', tag_edit, name="edit_tag"),


    # deletion
    path("admin/exercise/<int:pk>/delete", exercise_delete, name="delete_exercise"),
    path('admin/category/<int:pk>/delete', category_delete, name="delete_category"),
    path('admin/tag/<int:pk>/delete', tag_delete, name="delete_tag"),


    # authentification 
    path('account/register', signup, name='signup'),
    # path('compte/', include('django.contrib.auth.urls')),
    path('account/login', views.LoginView.as_view(), name='login'),
    path('account/logout', logout_view, name="logout"),
    path('accounts/profile/', profile, name="user_profile"),

     #ExerciseBuilder

   path('admin/exercise-builder', exercise_builder, name="exercise_builder"),

     # font 
   path('', index, name='index_front'),
   path('about', About.as_view(), name='about'),
   path('exercises', ExerciseListing.as_view(),name= 'exercises_list_font')

  
]
