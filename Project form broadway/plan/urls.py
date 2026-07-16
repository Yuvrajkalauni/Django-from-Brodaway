from django.urls import path
from plan.views import list_user_sub
urlpatterns = [
    path('',list_user_sub, name="user_sub"),

]