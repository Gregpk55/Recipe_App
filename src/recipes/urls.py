from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, search_recipes

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('search/', search_recipes, name='search_recipes')
]
