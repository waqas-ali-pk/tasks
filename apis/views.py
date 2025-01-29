from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer
from .permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, ]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, ]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
