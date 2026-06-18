from django.shortcuts import render,redirect
from todo.forms import TaskForm
from todo.models import Task
# Create your views here.

def home_task(request):
    data = Task.objects.all()
    context = {
        'data':data
    }
    return render(request,'home.html')



def create_task(request):
    data = TaskForm()
    if request.method == 'POST':
        data = request.POST
        form = TaskForm(data=data)
        if form.is_valid:
            form.save()
            return redirect ('home')
    return render(request,'create_task.html')
