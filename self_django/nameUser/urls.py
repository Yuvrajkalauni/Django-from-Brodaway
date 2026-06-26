
from django.urls import path
from nameUser.views import register


urlpatterns = [
    path('register/', register, name='register')
]


