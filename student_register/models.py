from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length = 50)





class Student(models.Model):
    fullname = models.CharField(max_length = 100)
    roll_no = models.CharField(max_length = 5)
    mobile = models.CharField(max_length = 10)
    position = models.ForeignKey(Position, on_delete = models.CASCADE)
