# Generated by Django 5.0.4 on 2024-04-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Breakfast", "Breakfast"),
                    ("Lunch", "Lunch"),
                    ("Dinner", "Dinner"),
                    ("Dessert", "Dessert"),
                    ("Other", "Other"),
                ],
                default="Other",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cooking_time",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="dietary_information",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="recipe_images/"),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="preparation_steps",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="serving_size",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
