from audioop import reverse
from inspect import formatannotation
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from CoachingDrills.forms import CustiomSignupForm, SignUpForm, ExerciseAddForm, TagAddForm, CategoryAddForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Exercise, Category, Tag
from django.shortcuts import render, get_object_or_404




# Cutom admin page
@login_required
def index(request):
    return render(request, 'index.html')

# User authentification views
def signup(request):
    context= {}

    if request.method == 'POST':
        form = CustiomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f'Bienvenue {request.POST.get("first_name")} !')
        else:
            context['errors'] = form.errors
    else: 
        form = CustiomSignupForm()

    context['form'] = form

    return render(request, 'signup.html', context=context)

def profile(request):
    context = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'username': request.user.username
    }
    return render(request, 'profile.html', context=context)

def logout_view(request):
    first_name = request.user.first_name
    logout(request)
    messages.add_message(request, messages.INFO, f'Merci {first_name}, au revoir.')
    return redirect('login')


# Listing views
@login_required
def exercices_listing(request):
    exercises = Exercise.objects.all()
    return render(request,'listing/exercises.html', context={'exercises': exercises})

@login_required
def categories_listing(request):
    categories = Category.objects.all()
    return render(request, 'listing/categories.html', context={'categories': categories})

@login_required
def tags_listing(request):
    tags = Tag.objects.all()
    return render(request,'listing/tags.html', context={'tags': tags})


# Creation views
@login_required
def exercise_add(request): 
    context = {}
    if request.method == 'POST':
        form = ExerciseAddForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExerciseAddForm()

    form = ExerciseAddForm()
    context['form'] = form

    return render(request, 'creation/exercise_creation.html', context=context)

@login_required
def category_add(request): 
    context = {}
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryAddForm()

    form = CategoryAddForm()
    context['form'] = form

    return render(request, 'creation/category_creation.html', context=context)

@login_required
def tag_add(request): 
    context = {}
    if request.method == 'POST':
        form = TagAddForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TagAddForm()

    form = TagAddForm()
    context['form'] = form

    return render(request, 'creation/tag_creation.html', context=context)


# Deletion views
@login_required
def exercise_delete(request, pk):

    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('exercice_listing')

    context={'exercise': exercise}
    return render(request, 'deletion/exercise_deletion.html', context=context)

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_listing')

    context = {'category': category}
    return render(request, 'deletion/category_deletion.html', context=context)

@login_required
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_listing')
    
    context = {'tag': tag}
    return render(request, 'deletion/tag_deletion.html', context=context)

# Detail views
@login_required
def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    context= {'exercise': exercise}
    return render(request, 'detail/exercise.html', context=context)

@login_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    exercises = Exercise.objects.filter(category=category)
    context = {'category': category, 'exercises': exercises}
    return render(request, 'detail/category.html', context=context)

@login_required
def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    context = {'tag': tag}
    return render(request, 'detail/tag.html', context=context)


# editing views
@login_required
def exercise_edit(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseAddForm(request.POST, instance=exercise)
        if form.is_valid:
            form.save()
            return redirect('exercise_listing')

    form = form = ExerciseAddForm(instance=exercise)
    context = {'form': form, 'exercise': exercise}

    return render(request, 'edit/exercise.html', context=context)

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryAddForm(request.POST, instance=category)
        if form.is_valid:
            form.save()
            return redirect('category_listing')

    form = form = CategoryAddForm(instance=category)
    context = {'form': form, 'category': category}

    return render(request, 'edit/category.html', context=context)

@login_required
def tag_edit(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagAddForm(request.POST, instance=tag)
        if form.is_valid:
            form.save()
            return redirect('tag_listing')

    form = form = TagAddForm(instance=tag)
    context = {'form': form, 'tag': tag}

    return render(request, 'edit/tag.html', context=context)


