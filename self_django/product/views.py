from django.shortcuts import redirect, render
from product.models import Items
# Create your views here.
def show_items(request):
    data = Items.objects.all()
    print(data)
    return render(request, "product/things.html", {"Products":data})

def create_product(request):
    if request.method == 'POST':
        data = request.POST
        Items.objects.create(
            name = data['P_name'],
            address = data['P_address'],
            phone_number = data['P_phone_number']
        )
        return redirect('/show_items')
    return render(request, "product/create_product.html")