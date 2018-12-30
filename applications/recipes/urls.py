from django.urls import path, re_path

from . import views

app_name="recipes_app"

urlpatterns = [
    path('recipes', views.RecipeList.as_view(), name="recipes"),
    path('recipes/add', views.AddRecipe.as_view(), name="addrecipe"),
    path('recipes/<pk>/ingredients', views.IngredientsRecipeList.as_view(), name="ingredients-recipe"),
    path('recipes/<pk>/edit', views.EditRecipe.as_view(), name="editrecipe"),
    path('recipes/<pk>/addingredient', views.AddIngredient.as_view(), name="addingredient")
]
