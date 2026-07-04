from django.urls import path
from meals.views import IngredientCreateView, IngredientDeleteView, IngredientListView, IngredientUpdateView, MealCreateView, MealDeleteView, MealIngredientCreateView, MealIngredientDeleteView, MealIngredientListView, MealIngredientUpdateView, MealListView, MealPlanCreateView, MealPlanDeleteView, MealPlanItemsCreateView, MealPlanItemsDeleteView, MealPlanItemsListView, MealPlanItemsUpdateView, MealPlanListView, MealPlanUpdateView, MealUpdateView

urlpatterns = [

    #------------------------------ Meal ------------------------------
    path('', MealListView.as_view(), name = 'meal-list'),
    path('create/', MealCreateView.as_view(), name = 'meal-create'),
    path('update/<int:pk>', MealUpdateView.as_view(), name = 'meal-update'),
    path('delete/<int:pk>', MealDeleteView.as_view(), name = 'meal-delete'),

    #------------------------------ MealPlan ------------------------------
    path('MealPlan/', MealPlanListView.as_view(), name = 'MealPlan-list'),
    path('MealPlan/create/', MealPlanCreateView.as_view(), name = 'MealPlan-create'),
    path('MealPlan/update/<int:pk>', MealPlanUpdateView.as_view(), name = 'MealPlan-update'),
    path('MealPlan/delete/<int:pk>', MealPlanDeleteView.as_view(), name = 'MealPlan-delete'),

    #------------------------------ MealPlanItem ------------------------------
    path('MealPlanItem/', MealPlanItemsListView.as_view(), name = 'MealPlanItem-list'),
    path('MealPlanItem/create/', MealPlanItemsCreateView.as_view(), name = 'MealPlanItem-create'),
    path('MealPlanItem/update/<int:pk>', MealPlanItemsUpdateView.as_view(), name = 'MealPlanItem-update'),
    path('MealPlanItem/delete/<int:pk>', MealPlanItemsDeleteView.as_view(), name = 'MealPlanItem-delete'),

    #------------------------------ Ingredient ------------------------------
    path('ingredient/', IngredientListView.as_view(), name = 'Ingredient-list'),
    path('ingredient/create/', IngredientCreateView.as_view(), name = 'Ingredient-create'),
    path('ingredient/update/<int:pk>', IngredientUpdateView.as_view(), name = 'Ingredient-update'),
    path('ingredient/delete/<int:pk>', IngredientDeleteView.as_view(), name = 'Ingredient-delete'),

    #------------------------------ MealIngredient ------------------------------
    path('MealIngredient/', MealIngredientListView.as_view(), name = 'MealIngredient-list'),
    path('MealIngredient/create/', MealIngredientCreateView.as_view(), name = 'MealIngredient-create'),
    path('MealIngredient/update/<int:pk>', MealIngredientUpdateView.as_view(), name = 'MealIngredient-update'),
    path('MealIngredient/delete/<int:pk>', MealIngredientDeleteView.as_view(), name = 'MealIngredient-delete'), 

    
]
