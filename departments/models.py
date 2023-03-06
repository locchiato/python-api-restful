from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def created_date(self):
        return self.created_at
# Create your models here.
