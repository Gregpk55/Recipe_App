from django.shortcuts import render     #imported by default
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe               #to access recipe model
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from .utils import get_chart
from django.urls import reverse
from .forms import RecipesSearchForm



class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = RecipesSearchForm(self.request.GET or None)
        return context

class RecipeDetailView(LoginRequiredMixin,DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

def home(request):
    return render(request, 'recipes/home.html')


def search_recipes(request):
    is_show_all = request.GET.get('show_all') == 'true'
    default_graph_data_type = 'difficulty' if is_show_all else 'cooking_time'
    graph_data_type = request.GET.get('graph_data_type', default_graph_data_type)
    chart_type = request.GET.get('chart_type', '#1') 
    form = RecipesSearchForm(initial={'graph_data_type': graph_data_type}, data=request.GET or None)
    recipes_df = None
    chart = None
    
    if request.GET.get('show_all') == 'true' or form.is_valid():
        search_term = form.cleaned_data.get('search') if form.is_valid() else None
        if search_term:
            name_matches = Recipe.objects.filter(name__icontains=search_term)
            ingredient_matches = Recipe.objects.filter(ingredients__icontains=search_term)
            queryset = name_matches | ingredient_matches
        else:
            queryset = Recipe.objects.all()
        
        if queryset.exists():
            chart_data_type = request.GET.get('graph_data_type', 'cooking_time')

            data = [
                {
                    'name': f'<a href="{reverse("recipes:recipe-detail", args=[recipe.id])}">{recipe.name}</a>',
                    'cooking_time': recipe.cooking_time,
                    'difficulty': recipe.difficulty(),
                    'ingredients': recipe.ingredients,
                    'description': recipe.description
                }
                for recipe in queryset
            ]
            
            df = pd.DataFrame(data)
            recipes_df = df.to_html(index=False, classes='table table-striped', escape=False)
            
        if chart_data_type == 'difficulty':
            difficulty_data = {'Easy': [], 'Medium': [], 'Intermediate': [], 'Hard': []}
            
            for recipe in queryset:
                difficulty_data[recipe.difficulty()].append(recipe.name)
            
            rows = []
            for difficulty, names in difficulty_data.items():
                count = len(names)
                recipe_names = ", ".join(names)
                rows.append({'difficulty': difficulty, 'count': count, 'recipe_names': recipe_names})
                
            difficulty_data_frame = pd.DataFrame(rows)
            chart = get_chart(chart_type, difficulty_data_frame, 'difficulty', queryset)

        elif chart_data_type == 'cooking_time':
            chart = get_chart(chart_type, df, 'cooking_time')

    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart,
    }
    
    return render(request, 'recipes/search_recipes.html', context)
