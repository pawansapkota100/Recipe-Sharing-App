from django.contrib import admin
from .models import Feed,Followers,Recipe,FavoriteRecipe,Review, Tag
# Register your models here.

admin.site.register(Feed)
admin.site.register(Followers)
admin.site.register(Recipe)
admin.site.register(FavoriteRecipe)
admin.site.register(Review)
admin.site.register(Tag)

