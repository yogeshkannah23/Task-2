# Generated by Django 5.1 on 2024-10-11 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0005_recipe_user_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=30)),
                ("description", models.CharField(blank=True, max_length=100)),
                ("ingredients", models.CharField(blank=True, max_length=100)),
                ("preparation_steps", models.CharField(blank=True, max_length=300)),
                ("cooking_time", models.DateField()),
                ("user_id", models.CharField(blank=True, max_length=300)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipe.category",
                        to_field="name",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Recipe",
        ),
    ]
