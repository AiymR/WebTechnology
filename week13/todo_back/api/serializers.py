from rest_framework import serializers
from .models import TaskList, Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        password = validated_data.get('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        return user
    class Meta:
        model =  User
        fields = ('id','username','email')
class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        return instance

    def create(self, validated_data):
        taskList = TaskList(**validated_data)
        taskList.save()
        return taskList


class SimpleSerializer(serializers.ModelSerializer):
	task_list = TaskListSerializer
	class Meta:
		model = Task
		fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list')


