from audioop import reverse
from inspect import formatannotation
from multiprocessing import context
from pyexpat import model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from CoachingDrills.forms import CustiomSignupForm, SignUpForm, ExerciseAddForm, TagAddForm, CategoryAddForm, FilterCategTag, FavouriteForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from blog.models import Exercise, Category, Tag, User, Favourite
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.views.generic import TemplateView, ListView, DetailView
import markdown as md




# Cutom admin page
@staff_member_required(login_url='login')
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
            return HttpResponse(f'Welcome {request.POST.get("first_name")} !')
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
    messages.add_message(request, messages.INFO, f'Goodbye {first_name}, see you later.')
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

    sort= request.GET.get('sort', False)
    authorized_sorting_field = [
        'name',
        'category',
        'duration',
        'number_of_player',
        'difficulty',
        'tag',
        '-name',
        '-category',
        '-duration',
        '-number_of_player',
        '-difficulty',
        '-tag'
    ]

    if sort:
        if sort in authorized_sorting_field:
            exercises = exercises.order_by(sort)


    

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
        form = ExerciseAddForm(request.POST, request.FILES)
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
        form = ExerciseAddForm(request.POST, request.FILES, instance=exercise)
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

# About

class About(TemplateView):
    template_name = 'font/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open('blog/markdown_texts/about.md', 'r', encoding='utf-8') as f:
            about = md.markdown(f.read())
        context['about'] = about
        return context

# listing
class ExerciseListing(ListView):
    model = Exercise
    template_name = 'font/listing/exercises_listing.html'
    context_object_name = 'exercises'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercises_count = self.object_list.count()
        form = FilterCategTag()
        context['form'] = form
        context['count'] = exercises_count
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(like_number=Count('likes'))
        queryset = queryset.annotate(user_like=Count('likes', filter=Q(likes__user=self.request.user)))
        if self.request.method == 'GET':
            form = FilterCategTag(self.request.GET)
            if form.is_valid():
                data = form.cleaned_data
                categories = data['categories']
                tags = data['tags'] 
                query= data['research']
                like = data['like']
                if like is True:
                    queryset = queryset.filter(user_like=1)
                if categories:
                    queryset = queryset.filter(category__in=categories)
                if tags:
                    queryset = queryset.filter(tag__in=tags)
                if query:
                    queryset = queryset.filter(Q(name__icontains=query)|Q(category__name__icontains=query)|Q(tag__name__icontains=query))
            # else:
            #     form = FilterCategTag()

        return queryset



def favourite(request, pk):
    if request.method == 'POST':
        exercise = get_object_or_404(Exercise, pk=pk)
        user = request.user
        check = Favourite.objects.filter(exercise=exercise, user=user)
        if not check:
            fav = Favourite(exercise=exercise, user=user)
            fav.save()
            message = 'liked'
        else:
            check.delete() 
            message = 'unliked' 
    return JsonResponse({'message': message})


class ExerciseDetails(DetailView):
    model = Exercise
    template_name = 'font/detail/exercises_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        instance.description = md.markdown(instance.description)
        context['object'] = instance
        return context
    

