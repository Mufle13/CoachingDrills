from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import Category, Favourite, Tag, User, Exercise

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
            'tag': 'Tag(s)',
            'duration': 'Duration',
            'number_of_player': 'Number of player',
            'difficulty': 'Difficulty',
            'picture': 'Illustration',
            'description': 'Description'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name','placeholder': 'Name of your exercise'}),
            'description': forms.Textarea(attrs={'class': 'description', 
            'placeholder': 'Description of the exercise'}),
            'category': forms.RadioSelect(attrs={'required': True}),
            'tag': forms.CheckboxSelectMultiple(attrs={'class': 'tags'})
            }

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]

class TagAddForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class ExerciseFilterForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Categories', widget=forms.CheckboxSelectMultiple, required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label='Tags', widget=forms.CheckboxSelectMultiple, required=False)
    research = forms.CharField(max_length=100, required=False)
    difficulty = forms.ChoiceField(choices=Exercise.difficulty.field.choices, label='Difficulty', required=False)
    number_of_player = forms.IntegerField(label='Number of players', required=False)
    

class FavouriteForm(forms.Form):
    class Meta:
        model = Favourite
        fields = '__all__'

