# Generated by Django 5.1 on 2024-10-11 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0009_alter_recipes_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipes",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipe.category",
                to_field="name",
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="owner",
            field=models.CharField(default="admin", max_length=30),
        ),
    ]
