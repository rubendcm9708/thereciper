from django.urls import path, re_path

from . import views

app_name="ingredients_app"

urlpatterns = [
    path('ingredients', views.IngredientList.as_view(), name="ingredient"),
    path('ingredients/add', views.AddIngredient.as_view(), name="addingredient"),
    path('ingredients/<pk>/edit', views.EditIngredient.as_view(), name="editingredient")
]
