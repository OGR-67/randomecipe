from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """A recipe defined by [API_id](INTEGER), [title](STRING), [image_url](STRING), [ingredients](JSON) and [instructions](JSON)."""
    API_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    image_url = models.TextField()
    ingredients = models.JSONField()
    instructions = models.JSONField()

    def __str__(self) -> str:
        return f"{self.title}"


class CurrentRecipe(models.Model):
    """A current highlighted recipe."""
    recipe = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return f"Recipe ID n°{self.recipe}"


class UserFavoriteRecipe(models.Model):
    """User and recipe association."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"[ {self.user} ] enjoyed [ {self.recipe} ]"
