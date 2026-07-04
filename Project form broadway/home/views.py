from django.shortcuts import render
from meals.models import Meal, MealPlan, MealPlanItems, Ingredient, MealIngredient

# Create your views here.

# def dashboard (request): 
#     meal = Meal.objects.all() 
#     meal_plan = MealPlan.objects.all() 
#     meal_plan_items = MealPlanItems.objects.all() 
#     ingredient = Ingredient.objects.all() 
#     meal_ingredient = MealIngredient.objects.all() 
#     context = { 
#         'meal':meal.count(), 
#         'meal_plan':meal_plan.count(), 
#         'meal_plan_items':meal_plan_items.count(), 
#         'ingredient':ingredient.count(), 
#         'meal_ingredient':meal_ingredient.count() 
#         } 
#     return render (request, 'home/base.html', context)

def dashboard(request):
    context = {
        'meal': Meal.objects.count(),
        'meal_plan': MealPlan.objects.count(),
        'meal_plan_items': MealPlanItems.objects.count(),
        'ingredient': Ingredient.objects.count(),
        'meal_ingredient': MealIngredient.objects.count(),
    }

    return render(request, 'home/dashboard.html', context)