from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
 
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Exercise(models.Model):
    FACILE = "FA"
    MOYEN = "MO"
    DIFFICILE = "DI"

    DIFFICULTY = [
    (FACILE, "Facile"),
    (MOYEN, "Moyen"),
    (DIFFICILE, "Difficile")
]

    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag, blank=True)
    duration = models.IntegerField(blank=True, null=True)
    number_of_player = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=2, choices=DIFFICULTY, default=FACILE)



    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
