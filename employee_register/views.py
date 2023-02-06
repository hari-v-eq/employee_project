from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from.models import Employee
from django.contrib import messages

# Create your views here.
def employee_list(request):
    
    context={'employee_list':Employee.objects.all()}
    messages.success(request, 'Welcome to the Employee List')
    return render (request,"employee_register/employee_list.html",context)

def employee_form(request,id=0):

    if request.method=="GET": 
        if id==0:
            form=EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)

            form=EmployeeForm(instance=employee)
            
        return render (request, "employee_register/employee_form.html",{'form':form})
    else:
        if id==0:

            form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee has been updated.')
        return redirect('/employee/list')

def employee_delete(request,id):
    messages.success(request, 'Your profile was Deleted.')
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')



