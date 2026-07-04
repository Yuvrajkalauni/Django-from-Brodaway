from django import forms
from meals.models import (
    Meal,
    MealPlan,
    MealPlanItems,
    Ingredient,
    MealIngredient,
)


# Meal Form

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 outline-none",
                "placeholder": "Enter meal name",
            }),

            "meal_type": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 outline-none",
            }),

            "prepare_time": forms.NumberInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 outline-none",
                "placeholder": "Preparation time (minutes)",
            }),

            "description": forms.Textarea(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 outline-none",
                "rows": 4,
                "placeholder": "Meal description...",
            }),
        }


# Meal Plan Form

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = "__all__"

        widgets = {
            "user": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),

            "title": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
                "placeholder": "Meal plan title",
            }),

            "start_date": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),

            "end_date": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),

            "generated_by_ai": forms.CheckboxInput(attrs={
                "class": "h-5 w-5 rounded text-emerald-600 focus:ring-emerald-500",
            }),

            "created_at": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),

            "updated_at": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),
        }


# Meal Plan Items Form

class MealPlanItemsForm(forms.ModelForm):
    class Meta:
        model = MealPlanItems
        fields = "__all__"

        widgets = {
            "meal_plan": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),

            "meal": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),

            "date": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),
        }



# Ingredient Form

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
                "placeholder": "Ingredient name",
            }),

            "unit": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
                "placeholder": "e.g. g, kg, ml, cup",
            }),

            "calories_per_100g": forms.NumberInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
                "step": "0.01",
            }),

            "protein_per_100g": forms.NumberInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
                "step": "0.01",
            }),

            "carbs_per_100g": forms.NumberInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
                "step": "0.01",
            }),

            "fat_per_100g": forms.NumberInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
                "step": "0.01",
            }),
        }



# Meal Ingredient Form


class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = MealIngredient
        fields = "__all__"

        widgets = {
            "meal": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),

            "ingredient": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
            }),

            "quantity": forms.NumberInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2.5 focus:ring-2 focus:ring-emerald-500 outline-none",
                "placeholder": "Quantity",
            }),
        }