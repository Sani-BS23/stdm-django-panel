from rest_framework import serializers
from todos.models import Todo
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    done_count = serializers.ReadOnlyField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'done_count']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Todos must have at least 3 characters')
        return value
