from audioop import reverse
from inspect import formatannotation
from django.http import HttpResponse
from django.shortcuts import redirect, render
from CoachingDrills.forms import CustiomSignupForm, SignUpForm, ExerciseAddForm, TagAddForm, CategoryAddForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Exercise, Category, Tag




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
    exercices = Exercise.objects.all()
    return render(request,'listing/exercices.html', context={'articles': exercices})

@login_required
def categories_listing(request):
    categories = Category.objects.all()
    return render(request, 'listing/categories.html', context={'articles': categories})

@login_required
def tags_listing(request):
    tags = Tag.objects.all()
    return render(request,'listing/tags.html', context={'articles': tags})

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

