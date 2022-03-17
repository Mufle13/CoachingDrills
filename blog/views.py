from audioop import reverse
from inspect import formatannotation
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from CoachingDrills.forms import CustiomSignupForm, SignUpForm, ExerciseAddForm, TagAddForm, CategoryAddForm, FilterCategTag
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Exercise, Category, Tag, User
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q




# Cutom admin page
@login_required
def admin_index(request):
    user = request.user
    context = {'user': user}

    return render(request, 'admin/admin_index.html', context=context)

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

    return render(request, 'registration/signup.html', context=context)

def profile(request):
    context = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'username': request.user.username
    }
    return render(request, 'registration/profile.html', context=context)

def logout_view(request):
    first_name = request.user.first_name
    logout(request)
    messages.add_message(request, messages.INFO, f'Merci {first_name}, au revoir.')
    return redirect('login')


# Listing views
@login_required
def exercices_listing(request):
    if request.method == 'GET':
        form = FilterCategTag(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            categories = data['categories']
            tags = data['tags'] 
            query= data['research']
            exercises = Exercise.objects.all()
            if categories:
                exercises = exercises.filter(category__in=categories)
            if tags:
                exercises = exercises.filter(tag__in=tags)
            if query:
                exercises = exercises.filter(Q(name__icontains=query)|Q(category__name__icontains=query)|Q(tag__name__icontains=query))
        else:
            form = FilterCategTag
    exercises_count = exercises.count()
    paginator = Paginator(exercises, 3)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    return render(request,'admin/listing/exercises.html', context={'exercises': exercises, 'page_obj': page_obj, 'form':form, 'exercises_count': exercises_count})

@login_required
def categories_listing(request):
    categories = Category.objects.all()
    return render(request, 'admin/listing/categories.html', context={'categories': categories})

@login_required
def tags_listing(request):
    tags = Tag.objects.all()
    return render(request,'admin/listing/tags.html', context={'tags': tags})


# Creation views
@login_required
def exercise_add(request): 
    context = {}
    if request.method == 'POST':
        form = ExerciseAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_listing')
    else:
        form = ExerciseAddForm()

    form = ExerciseAddForm()
    context['form'] = form

    return render(request, 'admin/creation/exercise_creation.html', context=context)

@login_required
def category_add(request): 
    context = {}
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_listing')
    else:
        form = CategoryAddForm()

    form = CategoryAddForm()
    context['form'] = form

    return render(request, 'admin/creation/category_creation.html', context=context)

@login_required
def tag_add(request): 
    context = {}
    if request.method == 'POST':
        form = TagAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_listing')
    else:
        form = TagAddForm()

    form = TagAddForm()
    context['form'] = form

    return render(request, 'admin/creation/tag_creation.html', context=context)


# Deletion views
@login_required
def exercise_delete(request, pk):

    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('exercise_listing')

    context={'exercise': exercise}
    return render(request, 'admin/deletion/exercise_deletion.html', context=context)

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_listing')

    context = {'category': category}
    return render(request, 'admin/deletion/category_deletion.html', context=context)

@login_required
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_listing')
    
    context = {'tag': tag}
    return render(request, 'admin/deletion/tag_deletion.html', context=context)

# Detail views
@login_required
def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    context= {'exercise': exercise}
    return render(request, 'admin/detail/exercise.html', context=context)

@login_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    exercises = Exercise.objects.filter(category=category)
    context = {'category': category, 'exercises': exercises}
    return render(request, 'admin/detail/category.html', context=context)

@login_required
def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    context = {'tag': tag}
    return render(request, 'admin/detail/tag.html', context=context)


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

    return render(request, 'admin/edit/exercise.html', context=context)

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

    return render(request, 'admin/edit/category.html', context=context)

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

    return render(request, 'admin/edit/tag.html', context=context)

#Exercise Builder
def exercise_builder(request):
    return render(request, 'admin/exercise_builder.html')

# font
def index(request):
    exercises = Exercise.objects.all()
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'font/index.html', context=context)

# listing
def font_exercises_listing(request):
    query = request.GET.get('search')
   
    if query:
        exercises = Exercise.objects.filter(Q(name__icontains=query)|Q(category__name__icontains=query)|Q(tag__name__icontains=query))
    else: 
        exercises = Exercise.objects.all()

    paginator = Paginator(exercises, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render (request, 'font/listing/font_exercises_listing.html', context={'exercises': exercises, 'page_obj':page_obj})


