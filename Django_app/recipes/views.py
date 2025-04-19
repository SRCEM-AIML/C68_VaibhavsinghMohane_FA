from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

def homepage(request):
    recipes = Recipe.objects.all()
    return render(request, 'homepage.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    return render(request, 'recipe_detail.html')

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


def custom_admin(request):
    recipes = Recipe.objects.all()
    return render(request, 'admin.html', {'recipes': recipes})
@require_POST
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect('custom_admin')

def get_recipe_data(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return JsonResponse({
        'name': recipe.name,
    })

@require_POST
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    form = RecipeForm(request.POST, request.FILES, instance=recipe)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)