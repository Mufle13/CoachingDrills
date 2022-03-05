from cProfile import label
from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import Category, Tag, User, Exercise

class CustiomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'profile_pic'
            ]

        

JOBS = (
    ('python', 'Développeur Python'),
    ('javascript', 'Développeur JavaScript'),
    ('csharp', 'Développeur C#')
)

class SignUpForm(forms.Form):
    pseudo = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    cgu_accept = forms.BooleanField( initial=True)
    job = forms.ChoiceField(choices=JOBS)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get('pseudo')
        if '$' in pseudo:
            raise forms.ValidationError('Le pseudo ne peut pas contenir le symbol $')
        return pseudo 

class ExerciseAddForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            'name',
            'category',
            'tag',
            'duration',
            'number_of_player',
            'difficulty',
            'picture',
            'description'
        ]
        labels = {'name': 'Title',
            'category': 'Category',
            'duration': 'Duration',
            'number_of_player': 'Number of player',
            'difficulty': 'Difficulty',
            'picture': 'Illustration',
            'description': 'Description'}
        widget = {
            'category': forms.SelectMultiple,
            'tag': forms.SelectMultiple
            }

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class TagAddForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'



