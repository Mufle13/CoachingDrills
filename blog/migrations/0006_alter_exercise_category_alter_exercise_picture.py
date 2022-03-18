# Generated by Django 4.0.2 on 2022-03-18 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='exercises_pic'),
        ),
    ]
