from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='In minutes')
    ingredients = models.CharField(
        max_length=350, 
        help_text='Ingredients must be separated by commas.'
    )
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def return_ingredients_as_list(self):
        return [ingredient.strip() for ingredient in self.ingredients.split(",")]

    def difficulty(self):
        ingredient_count = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and ingredient_count < 4:
            return "Easy"
        elif self.cooking_time < 10 and ingredient_count >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            return "Intermediate"
        else:
            return "Hard"

    def __str__(self):
        return str(self.name)
