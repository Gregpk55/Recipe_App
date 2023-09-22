from django.shortcuts import render     #imported by default
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe               #to access recipe model
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin,DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')

