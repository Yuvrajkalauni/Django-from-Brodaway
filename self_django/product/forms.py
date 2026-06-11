from django import forms
from product.models import Items

class Product_form(forms.ModelForm):
    class Meta:  # if we have to discribe forther more about class we use Meta.
        model = Items
        fields = '__all__' # this __all__ is used to select all the fields/attribute from models/table
      #  fields = ['name','address']  # to select specific fields/attributes form model/table