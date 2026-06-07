from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
    print("This is django views.")
    return HttpResponse("Hello world")

def json_home(request):
    # simple example of API
    y ={
        'Name' : 'Yuvraj',
        'Qualification' : 'Bachelor'
    }
    return JsonResponse(y) #jsonResponce is used in dictionary fuction

def detail(request):
    print(request.__dict__) # __dict__ is use to see detailed information about everything.
    return HttpResponse("Hi, I am Yuvraj kalauni.")

def show_complany(request):
    return render(request,'index.html', {"TechNova" : "UV_Solutions"})