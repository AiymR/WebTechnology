from rest_framework import serializers
from .models import TaskList, Task


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        return instance

    def create(self, validated_data):
        taskList = TaskList(**validated_data)
        taskList.save()
        return taskList


class TaskSerializer(serializers.ModelSerializer):
    task_list = TaskListSerializer

    class Meta:
        model = Task
        fields = ['id', 'name', 'created_at', 'due_on', 'status', 'task_list']

class SimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'status')

