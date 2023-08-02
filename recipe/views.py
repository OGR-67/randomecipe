from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator

from recipe.models import CurrentRecipe, Recipe, UserFavoriteRecipe


def index(request):
    recipes_list = _getCurrentRecipes()
    page_title = "Randomecipe - Home Page"
    context = {
        "page_title": page_title,
        "recipes_list": recipes_list,
        "query": "?page="
    }
    return render(request, "recipe/index.html", context)


def recipes(request):
    recipes_list = _getCurrentRecipes()
    favorites = []
    if request.user:
        favorites_query = UserFavoriteRecipe.objects.filter(
            user=request.user.id)
        favorites = [query_item.recipe for query_item in favorites_query]

    paginator = Paginator(recipes_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "page_title": "Randomecipe - Recipes Of The Week",
        "favorites": favorites,
    }
    return render(request, "recipe/recipes.html", context)


def _getCurrentRecipes():
    recipes_list = []
    current_recipe = CurrentRecipe.objects.all()
    for recipe in current_recipe:
        to_add = Recipe.objects.get(API_id=recipe.recipe)
        recipes_list.append(to_add)
    return recipes_list


@login_required
def favorites_recipes(request):
    recipes_list = UserFavoriteRecipe.objects.filter(user=request.user.id)

    # Make sure the data belongs to the current user
    for recipe in recipes_list:
        if recipe.user.id != request.user.id:  # type: ignore
            raise Http404

    paginator = Paginator(recipes_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "page_title": "Randomecipe - Favorite Recipes",
    }
    return render(request, "recipe/favorites_recipes.html", context)


@login_required
def add_favorite(request, recipe_id):
    if request.method == "POST":
        recipe = Recipe.objects.get(API_id=recipe_id)
        user = request.user
        new_favorite = UserFavoriteRecipe(
            user=user,
            recipe=recipe
        )
        new_favorite.save()
    return redirect("recipe:recipes")


@login_required
def del_favorite(request, recipe_id):
    if request.method == "POST":
        recipe = Recipe.objects.get(API_id=recipe_id)
        favorite = UserFavoriteRecipe.objects.get(
            recipe=recipe, user=request.user)
        favorite.delete()

    return redirect("recipe:favorites")
