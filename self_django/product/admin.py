from django.contrib import admin
from product.models import Items
# Register your models here.

# admin.site.register(Items)

@admin.register(Items)
class ProductAdminn(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number']
    list_filter = ['name', 'address']
    search_fields = ['phone_number']