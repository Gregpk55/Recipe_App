from django import forms
from .models import Recipe

CHART_TYPE_CHOICES = [
    ('', 'Select Chart Type'),
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart'),
]

GRAPH_DATA_TYPE_CHOICES = [
    ('cooking_time', 'Cooking Time'),
    ('difficulty', 'Difficulty'),
]


class RecipesSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search recipes or ingredients', 'class': 'search_input'}),
        help_text='Enter a recipe name or ingredient.'
    )
    chart_type = forms.ChoiceField(
        required=False,
        choices=CHART_TYPE_CHOICES,
        initial='#1',
        widget=forms.Select(attrs={'class': 'chart_type_select'}),
        help_text='Select the type of chart to display.'
    )
    graph_data_type = forms.ChoiceField(
        required=False,
        choices=GRAPH_DATA_TYPE_CHOICES,
        initial='cooking_time',
        widget=forms.Select(attrs={'class': 'graph_data_type_select'}),
        help_text='Select the type of data to plot.'
    )

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'cooking_time', 'description', 'pic']
        