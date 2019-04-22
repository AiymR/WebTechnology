from rest_framework import serializers
from .models import TaskList

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True);
    name = serializers.CharField(required=True);

    def create(self,validated_data):
        tasklist = TaskList(**validated_data)
        tasklist.save()
        return tasklist


    def update(self,instance,validated_data):
        instance.name = validated_data.get('get',instance.name)
        instance.save()
        return instance

