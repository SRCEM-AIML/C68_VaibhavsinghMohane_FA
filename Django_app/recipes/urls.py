from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('admin/', views.custom_admin, name='custom_admin'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('get_recipe_data/<int:recipe_id>/', views.get_recipe_data, name='get_recipe_data'),
    path('update_recipe/<int:recipe_id>/', views.update_recipe, name='update_recipe'),
]
