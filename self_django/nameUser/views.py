from django.shortcuts import render
from nameUser.forms import Register_form
# Create your views here.

def register(request):
    form = Register_form()
    context = {
        'form' : form
    }
    return render(request, 'user/index.html', context)