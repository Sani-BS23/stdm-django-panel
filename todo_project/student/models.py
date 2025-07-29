from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    @property
    def done_count(self):
        """
        Calculate the count of completed todos for this student on demand.
        This will be included when serializing the model.
        """
        return self.todos.filter(completed=True).count()
