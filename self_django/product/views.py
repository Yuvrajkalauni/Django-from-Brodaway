from django.shortcuts import render

# Create your views here.
def show_items(request):
    return render(request, "product/things.html")