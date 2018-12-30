from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView

from .models import Ingredient
# Create your views here.
class IngredientList(ListView):
    template_name = "ingredients/ingredientlist.html"
    model = Ingredient
    context_object_name = 'ingredients'

class AddIngredient(CreateView):
    template_name = "ingredients/addingredient.html"
    model = Ingredient
    fields = ['name','measure','quantity','price']
    success_url = '/ingredients'

class EditIngredient(UpdateView):
    template_name= "ingredients/editingredient.html"
    model = Ingredient
    fields = ['name','measure','quantity','price']
    success_url = '/ingredients'
    pk_url_kwarg = 'pk'
