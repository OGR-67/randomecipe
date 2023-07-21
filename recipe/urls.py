from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipes, name='recipes'),
    path('favorites-recipes/', views.favorites_recipes, name='favorites'),
    path('add-favorite/<int:recipe_id>',
         views.add_favorite, name='add_favorite'),
    path('del-favorite/<int:recipe_id>',
         views.del_favorite, name='del_favorite'),
]
