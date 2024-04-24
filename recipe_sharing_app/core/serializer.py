from .models import Recipe,Tag,Feed,FavoriteRecipe , Review
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'preparation_steps', 'cooking_time_minutes', 'serving_size', 'dietary_information', 'image', 'category', 'tags']


class FeedSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer() 
    class Meta:
        model = Feed
        fields = ['id','user', 'recipe', 'timestamp'] 

class FavoriteRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRecipe
        fields = '__all__'
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='__all__'