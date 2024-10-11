# Generated by Django 5.1 on 2024-10-11 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                ("description", models.CharField(blank=True, max_length=30)),
                ("ingredients", models.CharField(blank=True, max_length=30)),
                ("preparation_steps", models.CharField(blank=True, max_length=30)),
                ("cooking_time", models.CharField(blank=True, max_length=30)),
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
    ]
