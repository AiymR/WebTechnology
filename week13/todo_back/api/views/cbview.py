from ..models import TaskList,Task
from ..serializers import TaskListSerializer,SimpleSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

class TaskListList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        task_list = TaskList.objects.filter(owner=self.request.user)
        serializer = TaskListSerializer(task_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskListCrud(APIView):
    def get_object(self,pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            return Response({'error: not found'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
            task_list=self.get_object(pk)
            serializer = TaskListSerializer(task_list)
            return Response(serializer.data)

    def put(self,request,pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task_lists = self.get_object(pk)
        task_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Tasks(APIView):
    def get(self,request,pk):
        task_list = TaskList.objects.get(id=pk)
        tasks =  task_list.task_set.all()
        serializer = SimpleSerializer(tasks,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = JSONParser().parse(request)
        serializer = SimpleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Task_Detail(APIView):
    def get_object(self,pk):
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response({'error: not found'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        task = self.get_object(pk)
        serializer = SimpleSerializer(task)
        return Response(serializer.data)

    def put(self,request,pk):
        task = self.get_object(pk)
        serializer = SimpleSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request,pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def tasks_list(request, pk):
	if request.method == 'GET':
		task_lists = TaskList.objects.get(id=pk)
		tasks = task_lists.task_set.all()
		serializer = SimpleSerializer(tasks, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SimpleSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

