from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):       # this shows position title insted of position id or objects
        return self.title





class Student(models.Model):
    full_name = models.CharField(max_length = 100)
    roll_number = models.CharField(max_length = 5)
    mobile = models.CharField(max_length = 10)
    position = models.ForeignKey(Position, on_delete = models.CASCADE)
