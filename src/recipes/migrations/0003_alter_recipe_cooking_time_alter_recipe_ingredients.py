# Generated by Django 4.2.5 on 2023-10-03 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_cooking_time_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=350),
        ),
    ]
