from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from meals.forms import IngredientForm, MealForm, MealIngredientForm, MealPlanForm, MealPlanItemsForm
from meals.models import Ingredient, Meal, MealIngredient, MealPlan, MealPlanItems
from django.views.generic.edit import CreateView, DeleteView, UpdateView

#Creating view by using class base

#------------------------------ Meal ------------------------------

class MealListView(ListView):
    model = Meal
    paginate_by = 10
    template_name = 'meal/list.html'
    context_object_name = 'meals'

class MealCreateView(CreateView):
    model = Meal
    template_name = 'meal/create.html'
    form_class = MealForm
    success_url =  reverse_lazy('meal-list')

class MealUpdateView(UpdateView):
    model = Meal
    template_name = 'meal/update.html'
    form_class = MealForm
    success_url = reverse_lazy('meal-list')

class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'meal/delete.html'
    success_url = reverse_lazy('meal-list')

#------------------------------ MealPlan ------------------------------

class MealPlanListView(ListView):
    model = MealPlan
    paginate_by = 10
    template_name = 'mealplan/list.html'
    context_object_name = 'mealPlans'

class MealPlanCreateView(CreateView):
    model = MealPlan
    template_name = 'mealplan/create.html'
    form_class = MealPlanForm
    success_url =  reverse_lazy('MealPlan-list')

class MealPlanUpdateView(UpdateView):
    model = MealPlan
    template_name = 'mealplan/update.html'
    form_class = MealPlanForm
    success_url =  reverse_lazy('MealPlan-list')

class MealPlanDeleteView(DeleteView):
    model = MealPlan
    template_name = 'mealplan/delete.html'
    success_url =  reverse_lazy('MealPlan-list')


#------------------------------ MealPlanItems ------------------------------

class MealPlanItemsListView(ListView):
    model = MealPlanItems
    paginate_by = 10
    template_name = 'mealplanitem/list.html'
    context_object_name = 'MealPlanItems'

class MealPlanItemsCreateView(CreateView):
    model = MealPlanItems
    template_name = 'mealplanitem/create.html'
    form_class = MealPlanItemsForm
    success_url = reverse_lazy('MealPlanItem-list')

class MealPlanItemsUpdateView(UpdateView):
    model = MealPlanItems
    template_name = 'mealplanitem/update.html'
    form_class = MealPlanItemsForm
    success_url = reverse_lazy('MealPlanItem-list')

class MealPlanItemsDeleteView(DeleteView):
    model = MealPlanItems
    template_name = 'mealplanitem/delete.html'
    success_url = reverse_lazy('MealPlanItem-list')


#------------------------------ Ingredient ------------------------------

class IngredientListView(ListView):
    model = Ingredient
    paginate_by = 10
    template_name = 'ingredient/list.html'
    context_object_name = 'Ingredients'

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = 'ingredient/create.html'
    form_class = IngredientForm
    success_url = reverse_lazy('Ingredient-list')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = 'ingredient/update.html'
    form_class = IngredientForm
    success_url = reverse_lazy('Ingredient-list')

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredient/delete.html'
    success_url = reverse_lazy('Ingredient-list')


#------------------------------ MealIngredient ------------------------------

class MealIngredientListView(ListView):
    model = MealIngredient
    paginate_by = 10
    template_name = 'mealingredient/list.html'
    context_object_name = 'MealIngredients'

class MealIngredientCreateView(CreateView):
    model = MealIngredient
    template_name = 'mealingredient/create.html'
    form_class = MealIngredientForm
    success_url = reverse_lazy('MealIngredient-list')

class MealIngredientUpdateView(UpdateView):
    model = MealIngredient
    template_name = 'mealingredient/update.html'
    form_class = MealIngredientForm
    success_url = reverse_lazy('MealIngredient-list')

class MealIngredientDeleteView(DeleteView):
    model = MealIngredient
    template_name = 'mealingredient/delete.html'
    success_url = reverse_lazy('MealIngredient-list')


