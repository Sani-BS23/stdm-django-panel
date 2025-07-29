from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from student.models import Student
from todo_project.serializers import TodoSerializer


class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all().order_by('created_at')
        serializer = TodoSerializer(todos, many=True)
        return Response({'todos': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        todo_serializer = TodoSerializer(data=request.data)
        if not todo_serializer.is_valid():
            return Response({'error': todo_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        todo_serializer.save()
        return Response({'todos': todo_serializer.data}, status=status.HTTP_201_CREATED)


class TodoDetails(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)

        return Response({
            'message': 'Todo retrieved successfully.',
            'todo': TodoSerializer(todo).data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        data = request.data

        # Check for required fields
        required_fields = ['title', 'slug', 'content', 'student_id']
        if not all(data.get(field) for field in required_fields):
            return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

        # Get student object
        student = get_object_or_404(Student, id=data['student_id'])

        # Update todo
        todo.title = data['title']
        todo.slug = data['slug']
        todo.content = data['content']
        todo.student = student
        todo.save()

        return Response({
            'message': 'Todo updated successfully.',
            'todo': TodoSerializer(todo).data
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        print('Hello delete')
        todo = get_object_or_404(Todo, id=pk)
        print(todo.title)
        todo.delete()
        return Response({'message': 'Todo deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
