from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def add(request):
    form = EmployeeForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'add.html',{'form':form})
         
def show(request):
    employees = Employee.objects.all()

    return render(request, 'show.html', {'employees': employees})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'employee': employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')