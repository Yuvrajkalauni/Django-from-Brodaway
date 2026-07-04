from django import forms
from meals.models import Ingredient, Meal, MealIngredient, MealPlan, MealPlanItems

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'


class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = "__all__"


class MealPlanItemsForm(forms.ModelForm):
    class Meta:
        model = MealPlanItems
        fields = "__all__"


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = MealIngredient
        fields = "__all__"
