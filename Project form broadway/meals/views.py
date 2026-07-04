from django.shortcuts import render
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
    success_url = '/meal'

class MealUpdateView(UpdateView):
    model = Meal
    template_name = 'meal/update.html'
    form_class = MealForm
    success_url = '/meal'

class MealDeleteView(DeleteView):
    model = Meal
    success_url = '/meal'



#------------------------------ MealPlan ------------------------------

class MealPlanListView(ListView):
    model = MealPlan
    template_name = 'mealPlan/list.html'
    context_object_name = 'mealPlans'

class MealPlanCreateView(CreateView):
    model = MealPlan
    template_name = 'mealPlan/create.html'
    form_class = MealPlanForm
    success_url = '/meal/mealPlan'

class MealPlanUpdateView(UpdateView):
    model = MealPlan
    template_name = 'mealPlan/update.html'
    form_class = MealPlanForm
    success_url = '/meal/mealPlan'

class MealPlanDeleteView(DeleteView):
    model = MealPlan
    success_url = '/meal/mealPlan'


#------------------------------ MealPlanItems ------------------------------

class MealPlanItemsListView(ListView):
    model = MealPlanItems
    template_name = 'MealPlanItems/list.html'
    context_object_name = 'MealPlanItemss'

class MealPlanItemsCreateView(CreateView):
    model = MealPlanItems
    template_name = 'MealPlanItems/create.html'
    form_class = MealPlanItemsForm
    success_url = '/meal/MealPlanItems'

class MealPlanItemsUpdateView(UpdateView):
    model = MealPlanItems
    template_name = 'MealPlanItems/update.html'
    form_class = MealPlanItemsForm
    success_url = '/meal/MealPlanItems'

class MealPlanItemsDeleteView(DeleteView):
    model = MealPlanItems
    success_url = '/meal/MealPlanItems'


#------------------------------ Ingredient ------------------------------

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'Ingredient/list.html'
    context_object_name = 'Ingredients'

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = 'Ingredient/create.html'
    form_class = IngredientForm
    success_url = '/meal/Ingredient'

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = 'Ingredient/update.html'
    form_class = IngredientForm
    success_url = '/meal/Ingredient'

class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = '/meal/Ingredient'


#------------------------------ MealIngredient ------------------------------

class MealIngredientListView(ListView):
    model = MealIngredient
    template_name = 'MealIngredient/list.html'
    context_object_name = 'MealIngredients'

class MealIngredientCreateView(CreateView):
    model = MealIngredient
    template_name = 'MealIngredient/create.html'
    form_class = MealIngredientForm
    success_url = '/meal/MealIngredient'

class MealIngredientUpdateView(UpdateView):
    model = MealIngredient
    template_name = 'MealIngredient/update.html'
    form_class = MealIngredientForm
    success_url = '/meal/MealIngredient'

class MealIngredientDeleteView(DeleteView):
    model = MealIngredient
    success_url = '/meal/MealIngredient'


