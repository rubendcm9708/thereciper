from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeIngredient

admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
