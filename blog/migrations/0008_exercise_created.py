# Generated by Django 4.0.2 on 2022-05-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_like_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
