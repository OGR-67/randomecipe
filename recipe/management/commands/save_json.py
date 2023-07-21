from django.core.management.base import BaseCommand
from recipe.models import Recipe
from recipe.models import CurrentRecipe
from typing import List, Dict
import json


class Command(BaseCommand):
    help = 'Save current JSON file to database.'

    def handle(self, *args, **kwargs):

        with open('data.json') as json_file:
            data: Dict[str, List[
                Dict[str, str]
            ]] = json.load(json_file)

            CurrentRecipe.objects.all().delete()
            number_of_file: int = 0

            for recipe in data["meals"]:
                if number_of_file == 5:
                    break
                ingredients: List[str] = [
                    (f'{recipe[f"strMeasure{i}"]}: {recipe[f"strIngredient{i}"]}')
                    for i in range(1, 21)
                    if recipe[f"strIngredient{i}"]
                ]
                new_data = Recipe()
                current_recipe = CurrentRecipe()
                new_data.API_id = int(recipe["idMeal"])
                current_recipe.recipe = new_data.API_id
                new_data.title = recipe["strMeal"]
                new_data.image_url = recipe["strMealThumb"]
                new_data.instructions = recipe["strInstructions"]\
                    .replace('. ', '.|endOfLine|')\
                    .split('|endOfLine|')
                new_data.ingredients = ingredients
                new_data.save()
                current_recipe.save()
                number_of_file += 1

        self.stdout.write(f"Saved {number_of_file} files to DB.")
