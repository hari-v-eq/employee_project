from dataclasses import field
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields= '__all__'
        # labels={
        #     'fullname': 'Full Name',
        #     'emp_code': 'Emp. Code', 
        #     }

    # def __init__(self,*args,**kwargs):
    #     super(EmployeeForm).__init__(*args,**kwargs)
    #     self.fields['position'].empty_label="Select"
