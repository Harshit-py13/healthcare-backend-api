from django.db import models

# Create your models here.
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()
    hospital = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name