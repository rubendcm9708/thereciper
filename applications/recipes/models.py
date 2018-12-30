from django.db import models
from applications.ingredients.models import Ingredient

# Create your models here.
class Recipe(models.Model):

    name = models.CharField('name', max_length=80, blank=False, null = False)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = quantity = models.DecimalField('quantity', max_digits=10, decimal_places=3, blank=False, null = False)
    
