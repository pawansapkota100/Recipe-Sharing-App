from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    DESSERT = 'Dessert'
    OTHER = 'Other'

    CATEGORY_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (DESSERT, 'Dessert'),
        (OTHER, 'Other'),  # Add "Other" as a default category
    ]

    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    REVIEW_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    preparation_steps = models.TextField(blank=True, null=True)
    cooking_time_minutes = models.IntegerField(blank=True, null=True, help_text="Enter cooking time in minutes")
    serving_size = models.CharField(max_length=50, blank=True, null=True)
    dietary_information = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTHER, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    review_status = models.CharField(max_length=20, choices=REVIEW_STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return self.title
    
class Feed(models.Model):
    user = models.ForeignKey(User, related_name='feed', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.recipe.title)

class Followers(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="follows_user")
    follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_by")

    def __str__(self):
        return str(f"{self.follower} follows {self.follows}")
    
    class Meta:
        unique_together = ('follower', 'follows')


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.recipe.title}"



class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f"Review by {self.user.username} for {self.recipe.title}"