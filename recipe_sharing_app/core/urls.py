from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .viewset import FollowViewSet,FeedListView,FavoriteRecipeViewSet,RecipeViewSet,ReviewViewSet

router = SimpleRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'favorite-recipes', FavoriteRecipeViewSet, basename='favorite-recipe')
router.register(r'recipes/(?P<recipe_pk>\d+)/reviews', ReviewViewSet, basename='review')




follow_viewset = FollowViewSet.as_view({
    'post': 'follow',
    'delete': 'unfollow'
})
urlpatterns = [
    path("", include(router.urls)),
    path("", include(router.urls)),
    path('follow/<int:pk>/', FollowViewSet.as_view({'post': 'follow'}), name='follow'),
    path('unfollow/<int:pk>/', FollowViewSet.as_view({'post': 'unfollow'}), name='unfollow'),
    path('feed/', FeedListView.as_view(), name='feed-list'),
]