from audioop import reverse
from inspect import formatannotation
from django.http import HttpResponse
from django.shortcuts import redirect, render
from CoachingDrills.forms import CustiomSignupForm, SignUpForm, ExerciseAddForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.

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

    return render(request, 'exercise_creation.html', context=context)

