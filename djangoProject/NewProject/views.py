from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentForm
from django.http import HttpResponse


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_view')
        else:
            return HttpResponse('invalid format try again')
    else:
        form = StudentForm()
        context = {'form': form}
        return render(request, 'NewProject/student_form.html', context)


def student_retrieve(request):
    student = Students.objects.all()
    context = {
        'student': student
    }
    return render(request, 'NewProject/student_list.html', context)


def student_retrieve_id(request, pk):
    try:
        student = Students.objects.get(id=pk)
    except Students.DoesNotExist:
        return HttpResponse("data doesn't found")
    else:
        context = {
            'student': student
        }
        return render(request, 'NewProject/student_detail.html', context)


def student_update(request, pk):
    if request.method == 'POST':
        student = Students.objects.get(id=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_view')
        else:
            context = {
                'error': 'data not found'
            }
            return render(request, 'NewProject/student_update.html', context)
    else:
        try:
            student = Students.objects.get(id=pk)
        except Students.DoesNotExist:
            return HttpResponse("Student data doesn't exist")
        else:
            context = {
                'student': student
            }
            return render(request, 'NewProject/student_update.html', context)


def student_delete(request, pk):
    student = Students.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        context = {
            'success': 'data deleted successfully'
        }
        return render(request, 'NewProject/student_delete.html', context)
    else:
        try:
            context = {
                'student': student
            }
            return render(request, 'NewProject/student_delete.html', context)
        except Students.DoesNotExist:
            context = {
                'error': "data doesn't exist"
            }
            return render(request, 'NewProject/student_delete.html', context)
