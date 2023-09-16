from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):

    def setUp(self):
        Recipe.objects.create(
            name='Ice Water',
            cooking_time=1,
            ingredients='Ice, Water',
            description='Refreshing Ice Water'
        )

    def test_return_ingredients_as_list(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.return_ingredients_as_list(), ['Ice', 'Water'])

    def test_difficulty(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.difficulty(), 'Easy')

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), recipe.name)