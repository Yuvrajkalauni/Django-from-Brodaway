from django.urls import path
from todo.views import home_task, create_task

urlpatterns = [
    path('home_view/',home_task, name='home'),
    path('create_task/',create_task, name='create')
]
