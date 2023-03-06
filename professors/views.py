from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404 

from departments.models import Department

from professors.models import Professor
from professors.forms import ProfessorForm

# Create your views here.
def index(request):
    context = {
        'professors': Professor.objects.all().order_by('-id')
    }

    return render(request, 'professors/index.html', context or None)


def create(request):
    form = ProfessorForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        department = Department.objects.get(name=form.cleaned_data['department'].name)
        
        professor = Professor.objects.create(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            gender=form.cleaned_data['gender'],
            department=department
        )

        return redirect('professors:index')

    context = {
        'form': form
    }

    return render(request, 'professors/create.html', context)
 
 

def detail(request, pk):
    professor = Professor.objects.get(pk=pk)
    return render(request, 'professors/details.html', professor)



def delete(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    professor.delete()

    return redirect('professors:index')


def update(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, initial={
        'name': professor.name,
        'surname': professor.surname,
        'gender': professor.gender
    })

    if request.method == 'POST' and form.is_valid():
        professor.name = form.cleaned_data['name']
        professor.surname = form.cleaned_data['surname']
        professor.gender = form.cleaned_data['gender']
        professor.department = form.cleaned_data['department']
        professor.save()

        return redirect('professors:index')

    context = {
        'form': form,
        'professor': professor
    }

    return render(request, 'professors/update.html', context)