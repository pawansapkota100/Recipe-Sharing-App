from django.db.models import Q
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics,status
from .models import Recipe,Feed,FavoriteRecipe,Review
from .serializer import RecipeSerializer,FeedSerializer,FavoriteRecipeSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Feed, Followers
from .serializer import FeedSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class RecipeFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Recipe.CATEGORY_CHOICES)

    class Meta:
        model = Recipe
        fields = ['category', 'tags'] 

  
class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'ingredients', 'tags__name']
    ordering_fields = ['cooking_time_minutes']
    filterset_class = RecipeFilter  




class FollowViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def follow(self, request, pk=None):
        user_to_follow = get_object_or_404(User, pk=pk)
        
        # Check if the user is already being followed
        if Followers.objects.filter(follower=request.user, follows=user_to_follow).exists():
            return Response({'message': 'You are already following this user'})
        
        # Create a new Followers instance to represent the follow relationship
        Followers.objects.create(follower=request.user, follows=user_to_follow)
        return Response({'message': 'You are now following this user'})

    def unfollow(self, request, pk=None):
        user_to_unfollow = get_object_or_404(User, pk=pk)
        
        # Check if the user is not being followed
        if not Followers.objects.filter(follower=request.user, follows=user_to_unfollow).exists():
            return Response({'message': 'You are not following this user'})
        
        # Remove the Followers instance representing the follow relationship
        Followers.objects.filter(follower=request.user, follows=user_to_unfollow).delete()
        return Response({'message': 'You have unfollowed this user'})

        

class FeedListView(generics.ListAPIView):
    serializer_class = FeedSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the user IDs of the users that the current user follows
        following_user_ids = Followers.objects.filter(follower=self.request.user).values_list('follows_id', flat=True)
        # Get the feed items of the users the current user follows
        queryset = Feed.objects.filter(user_id__in=following_user_ids)

        return queryset


class FavoriteRecipeViewSet(viewsets.ModelViewSet):
    queryset = FavoriteRecipe.objects.all()
    serializer_class = FavoriteRecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset to retrieve only the favorite recipes of the current user
        return FavoriteRecipe.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user field to the current user when creating a favorite recipe
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"message": "You do not have permission to delete this favorite recipe."},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        recipe_id = self.kwargs.get('recipe_pk')
        recipe = Recipe.objects.get(pk=recipe_id)
        serializer.save(user=self.request.user, recipe=recipe)