# Model Form 
from django.forms import ModelForm
from departments.models import Department

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name']

