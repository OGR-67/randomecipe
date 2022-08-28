from django.core.management.base import BaseCommand
from recipe.models import Recipe
from recipe.models import CurrentRecipe
import json

class Command(BaseCommand):
    help = 'Save current JSON file to database.'

    def handle(self, *args, **kwargs):
        with open('data.json') as json_file:
            data = json.load(json_file)
        
        number_of_file = 0
        CurrentRecipe.objects.all().delete()
        for recipe in data:
            new_data = Recipe()
            current_recipe = CurrentRecipe()
            new_data.API_id = recipe["id"]
            current_recipe.recipe = new_data.API_id
            new_data.title = recipe["title"]
            new_data.image_url = recipe["image"]
            new_data.instructions = recipe["instructions"]
            new_data.ingredients = recipe["ingredients"]
            new_data.save()
            current_recipe.save()
            number_of_file += 1
        
        self.stdout.write(f"Saved {number_of_file} files to DB.")