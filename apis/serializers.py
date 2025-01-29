from rest_framework import serializers

from .models import Task, Label


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = '__all__'
