from rest_framework import serializers
from .models import Todo
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email']


class TodoSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    student_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'slug', 'content', 'completed', 'created_at', 'updated_at', 'student', 'student_id']

    def create(self, validated_data):
        student_id = validated_data.pop('student_id')
        student = Student.objects.get(id=student_id)
        todo = Todo.objects.create(student=student, **validated_data)
        return todo

    def update(self, instance, validated_data):
        if 'student_id' in validated_data:
            student_id = validated_data.pop('student_id')
            instance.student = Student.objects.get(id=student_id)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
