from django.db import models

class Student(models.Model):
    name= models.CharField(max_length=30)
    age=models.IntegerField()

    def __str__(self):
        return self.name