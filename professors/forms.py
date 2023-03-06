# Model Form 
from django.forms import ModelForm
from professors.models import Professor

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['name','surname','gender','department']

