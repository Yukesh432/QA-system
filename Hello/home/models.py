from django.db import models

# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length=150, blank=True)
    date= models.DateField()

    def __str__(self):
        return self.question


