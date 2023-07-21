from django.contrib import admin
from .models import Recipe
from .models import CurrentRecipe
from .models import UserFavoriteRecipe

admin.site.register(Recipe)
admin.site.register(CurrentRecipe)
admin.site.register(UserFavoriteRecipe)
