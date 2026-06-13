from django.urls import path
from product.views import show_items, WOF_create_product, WF_create_product, Product_update, Product_delete

urlpatterns = [
    path('show_items/', show_items),
    path("WF_create_product/", WF_create_product),
    path("update_product/<int:id>", Product_update),
    path("delete/<int:id>", Product_delete),
    path('whithout_form.py_create_product/', WOF_create_product)
]