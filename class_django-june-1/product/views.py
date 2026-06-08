from django.shortcuts import render

# Create your views here.
def product_list(request):
    data = Product.objects.all()
    print(data)
    return render(request, "itmes/things.html" )
