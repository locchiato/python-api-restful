from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404 

from departments.models import Department
from departments.forms import DepartmentForm

# Create your views here.
def index(request):
    context = {
        'departments': Department.objects.all().order_by('-id')
    }

    return render(request, 'departments/index.html', context)


def create(request):
    form = DepartmentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        department = Department.objects.create(
            name=form.cleaned_data['name']
        )

        return redirect('departments:index')

    context = {
        'form': form
    }

    return render(request, 'departments/create.html', context)
 
 

def detail(request, pk): 
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'departments/details.html', department)



def delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()

    return redirect('departments:index')


def update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, initial={
        'name': department.name
    })

    if request.method == 'POST' and form.is_valid():
        department.name = form.cleaned_data['name']
        department.save()

        return redirect('departments:index')

    context = {
        'form': form,
        'department': department
    }

    return render(request, 'departments/update.html', context)