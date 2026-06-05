from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def intro(request):
    return HttpResponse("Hello I am Yuvraj and i will become king.")

# def item_list(request):
#     return render(request, )