from django.shortcuts import redirect, render
from school.models import Student, Teacher
from school.forms import Student_form, Teacher_form


# Create your views here.

#for student only

def student_view(request):
    data = Student.objects.all()
    context = {
        'students':data
    }
    return render(request,'student/student_view.html',context)

def student_add(request):
    form = Student_form()
    if request.method == 'POST':
        data = request.POST
        form = Student_form(data=data)
        if form.is_valid:
            form.save
            return redirect('student/student_view')
    context = {
        'form':form
    }
    return render(request, 'student/form.html', context)




#for teacher only

def teacher_view(request):
    data = Teacher.objects.all()
    context = {
        'teachers':data
    }
    return render(request,'teacher/teacher_view.html',context)


def teacher_add(request):
    form = Teacher_form()
    if request.method == 'POST':
        data = request.POST
        form = Teacher_form(data=data)
        if form.is_valid:
            form.save
            return redirect('school/ teacher/teacher_show/')
    context = {
        'form':form
    }
    return render(request, 'teacher/form.html', context)


# def teacher_update(request,id):
#     product = Teacher.objects.get(id)
#     form = Teacher_form(instance = product)
#     if request.method == 'POST':
#         data = request.POST
#         form = Teacher_form(instance=product, data=data)
#         if form.is_valid:
#             form.save()
#             return redirect('/teacher_view')
#     context = {
#         "form":form
#     }
#     return render(request, 'teacher/update_teacher.html', context)

    

    