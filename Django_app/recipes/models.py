from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipe_images/')

    def __str__(self):
        return self.name
