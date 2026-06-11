"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home , json_home, detail, show_complany
from product.views import show_items, WOF_create_product, WF_create_product, Product_update, Product_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('dictionary/', json_home),
    path('detail/', detail),
    path('company/',show_complany),
    path('show_items/', show_items),
    path("WF_create_product/", WF_create_product),
    path("update_product/<int:id>", Product_update),
    path("delete/<int:id>", Product_delete),
    path('whithout_form.py_create_product/', WOF_create_product)
]