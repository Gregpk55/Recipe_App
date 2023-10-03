from django.urls import path
from .views import create_recipe 
from .views import home, RecipeListView, RecipeDetailView, search_recipes, signup_view

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),  
    path('recipes/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('search/', search_recipes, name='search_recipes'),
    path('recipes/create/', create_recipe, name='create-recipe'),
]
