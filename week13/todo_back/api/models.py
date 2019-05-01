from django.db import models
from django.contrib.auth.models import User

class TaskListManager(models.Model):
    def for_user(self,user):
        self.filter(owner=user)

class TaskList(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default = None)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=255)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, default=None)

    def to_json_short(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }

    def to_json_long(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.__str__(),
            'due_on': self.due_on.__str__(),
            'status': self.status,
            'task_list': self.task_list.to_json(),
        }
