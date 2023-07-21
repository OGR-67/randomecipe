from django.core.management.base import BaseCommand
from recipe.models import Recipe
from recipe.models import CurrentRecipe


class Command(BaseCommand):
    help = "Clear recipes and current-recipes tables content."

    def handle(self, *args, **kwargs):
        Recipe.objects.all().delete()
        CurrentRecipe.objects.all().delete()
        self.stdout.write("Tables content deleted")
