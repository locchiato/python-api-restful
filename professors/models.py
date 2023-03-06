from django.db import models
from departments.models import Department

class Professor(models.Model):
    GENDERS = (
        ('H', 'Hombre'),
        ('M', 'Mujer')
    )
    
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=1, null=False, choices=GENDERS)
    department = models.ForeignKey(Department, related_name="professors", on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    @property
    def created_date(self):
        return self.created_at
    
    @property
    def prof_gender(self):
        return self.gender
        
# Create your models here.
