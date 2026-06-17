from django.shortcuts import redirect, render
from product.models import Items
from product.forms import Product_form
# Create your views here.
def show_items(request):
    data = Items.objects.all()
    print(data)
    return render(request, "product/things.html", {"Products":data}) 


# without_using_form but_using_ORM create product
def WOF_create_product(request):
    if request.method == 'POST':  #check weather form method id post or get
        data = request.POST       # all the data given by user through form is now copyed into data variable
        Items.objects.create(
            name = data['P_name'],
            address = data['P_address'],            # data is copyed into table data is selected using input field name = 'P_address'
            phone_number = data['P_phone_number']
        )
        return redirect('/show_items')     #This redirects user to show_items web page which let them view created product
    return render(request, "product/WOF_create_product.html")

# With_using_form create product
def WF_create_product(request):
    form = Product_form()
    if request.method == 'POST':
        data = request.POST
        form = Product_form(data=data)
        if form.is_valid:
            form.save()
            return redirect('/show_items')
    context = {
        "form":form
    }
    return render(request, 'product/WF_create_product.html', context)

# Update product data
def Product_update(request,id):
    product = Items.objects.get(id=id)
    form = Product_form(instance = product)
    if request.method == 'POST':
        data = request.POST
        form = Product_form(instance=product, data=data)
        if form.is_valid:
            form.save()
            return redirect('/show_items')
    context = {
        "form":form
    }
    return render(request, 'product/update_product.html', context)

# Delete Product data
def Product_delete(request,id):
    product = Items.objects.get(id=id)
    product.delete()
    return redirect('/show_items')

