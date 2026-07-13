from django.shortcuts import render
from plan.models import UserSubscription

# Create your views here.

def list_user_sub(request):
    user_sub = UserSubscription.objects.all()
    context = {
        "user_sub": user_sub
        }
    return render(request, "usersub/list.html", context)