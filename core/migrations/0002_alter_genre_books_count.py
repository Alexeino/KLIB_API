# Generated by Django 4.0.2 on 2022-02-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='books_count',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
