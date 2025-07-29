from django.db import models

from student.models import Student


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationship: connect to People
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title
