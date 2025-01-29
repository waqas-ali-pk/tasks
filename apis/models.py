from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

User = get_user_model()


class Label(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(fields=('name', 'owner'), name='unique_label'),
        ]


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.ManyToManyField(Label, related_name='task', through='TaskLabel')

    def __str__(self):
        return self.title


class TaskLabel(models.Model):
    Task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self):
        return self.label.name
