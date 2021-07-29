from django.shortcuts import render
from.serializers import TaskSerializer
from.models import Task
from rest_framework import generics, permissions


# Create your views here.

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Only an authenticated user can access this API
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer
