# Generated by Django 5.1 on 2024-10-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0008_remove_recipes_user_id_recipes_owner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipes",
            name="owner",
            field=models.CharField(default="yogesh", max_length=30),
        ),
    ]
