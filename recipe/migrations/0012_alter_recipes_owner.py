# Generated by Django 5.1 on 2024-10-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0011_alter_recipes_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipes",
            name="owner",
            field=models.IntegerField(default=1),
        ),
    ]
