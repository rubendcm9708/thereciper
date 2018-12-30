from django.shortcuts import render

from django.views.generic import TemplateView, ListView, UpdateView, CreateView

from .models import Recipe, RecipeIngredient
# Create your views here.
class RecipeList(ListView):
    template_name = "recipes/recipelist.html"
    model = Recipe
    context_object_name = 'recipes'

class IngredientsRecipeList(ListView):
    template_name = 'recipes/ingredients-recipelist.html'
    context_object_name = 'ingredientsrecipes'

    def get_queryset(self):
        id = self.kwargs['pk']
        list = RecipeIngredient.objects.filter(
            recipe_id = id
        )
        return list

class AddRecipe(CreateView):
    template_name = "recipes/addrecipe.html"
    model = Recipe
    fields = ['name']
    success_url = '/recipes'

class EditRecipe(UpdateView):
    template_name= "recipes/editrecipe.html"
    model = Recipe
    fields = ['name']
    success_url = '/recipes'
    pk_url_kwarg = 'pk'

class AddIngredient(CreateView):
    template_name = "recipes/addingredient.html"
    model = RecipeIngredient
    fields = ['recipe','ingredient','quantity']
    success_url = '/recipes'
    def get_queryset(self):
        id = self.kwargs['pk']
        list = RecipeIngredient.objects.filter(
            recipe_id = id
        )
        price = 0
        for i in list:
            price += ((i.quantity)*(i.ingredient.price))/(i.ingredient.quantity)
        return price
