from inspect import formatannotation
import django
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from blog.models import User

# Create your views here.

class CustiomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

def signup(request):
    context= {}

    if request.method == 'POST':
        form = CustiomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Bienvenue !')
        else:
            context['errors'] = form.errors

  
    form = CustiomSignupForm()
    context['form'] = form

    return render(request, 'signup.html', context=context)

