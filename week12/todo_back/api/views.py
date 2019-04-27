from django.shortcuts import render
from .models import TaskList, Task
from django.http import JsonResponse
import json
from .serializers import TaskListSerializer, SimpleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.parsers import JSONParser

@csrf_exempt
def task_list(request):
    if request.method=='GET':
        task_list=TaskList.objects.all()
        serializer=TaskListSerializer(task_list,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        body=json.loads(request.body)
        serializer=TaskListSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error':'bad request'})

@csrf_exempt
def tasklist_detail(request, pk):
    try:
        category = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(category)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        # check PUT
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save() # update function in serializer class
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({}, status=204)




@csrf_exempt
def todo_detail(request, pk):
    try:
        category = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = SimpleSerializer(category)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        # check PUT
        data = json.loads(request.body)
        serializer = SimpleSerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save() # update function in serializer class
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({}, status=204)


@csrf_exempt
def tasklist_task(request, pk):
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