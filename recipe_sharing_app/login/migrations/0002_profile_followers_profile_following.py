# Generated by Django 5.0.4 on 2024-04-23 09:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="followers",
            field=models.ManyToManyField(
                blank=True,
                related_name="following_profiles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="following",
            field=models.ManyToManyField(
                blank=True,
                related_name="follower_profiles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
