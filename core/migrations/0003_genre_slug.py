# Generated by Django 3.2.9 on 2022-02-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_genre_books_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]