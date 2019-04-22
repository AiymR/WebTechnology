from django.shortcuts import render
from .models import TaskList, Task
from django.http import JsonResponse
import json
from .serializers import TaskListSerializer, TaskSerializer, SimpleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import serializers

# def task_list_list(request):
#         task_lists = TaskList.objects.all()
#         json_task_lists = [t.to_json() for t in task_lists]
#         return JsonResponse(json_task_lists, safe=False)
#
# def task_list_detail(request, pk):
#         try:
#             task_list = TaskList.objects.get(id=pk)
#         except TaskList.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
#         return JsonResponse(task_list.to_json())

@csrf_exempt
def tasklist_list(request):
    if request.method == 'GET':
        categories = TaskList.objects.all()
        serializer = TaskListSerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save() # create function in serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)

    # POST doesnt work

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


# def task_list(request, pk):
#         try:
#             task_list = TaskList.objects.get(id=pk)
#         except TaskList.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
#
#         tasks = task_list.task_set.all()
#         json_tasks = [t.to_json_short() for t in tasks]
#
#         return JsonResponse(json_tasks, safe=False)
#
#
# def task_detail(request, pk):
#         try:
#             task = Task.objects.get(id=pk)
#         except Task.DoesNotExist as e:
#             return JsonResponse({'error': str(e)})
#
#         return JsonResponse(task.to_json_long())

@csrf_exempt
def todo_list(request,pk):
    try:
        categories = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        # category = categories.task_set.all()
        category = categories.objects.all()
        serializer = TaskListSerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def todo_detail(request, pk):
    try:
        category = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskSerializer(category)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        # check PUT
        data = json.loads(request.body)
        serializer = TaskSerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save() # update function in serializer class
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({}, status=204)

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
def detailed_task_list(request, pk):
    try:
        task = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    if request.method=='GET':
        serializer=TaskListSerializer(task_list)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        body=json.loads(request.body)
        serializer=TaskListSerializer(data=body, instance=task)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error':'bad request'})
    elif request.method=='DELETE':
        task.delete()
        return JsonResponse({})
    return JsonResponse({'error':'bad request'})

@csrf_exempt
def list_of_task_list(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
        tasks=task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    except TaskList.DoesNotExist as e:
        return  JsonResponse({'error':str(e)},safe=False)

@csrf_exempt
def detailed_task(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer=TaskSerializer(task)
        return JsonResponse(serializer.data)
    except Task.DoesNotExist as e:
        return JsonResponse({'error':str(e)}, safe=False)


def tasks_list(request, pk):
    try:
        tasks_list = TaskList.objects.get(id = pk)
    except TaskList.DoesNotExist as error:
        return Response({'error': str(error)})

    if request.method == "GET":
        tasks = tasks_list.task_set.all()
        serializer = SimpleSerializer(tasks, many=True)
        return Response(serializer.data)

@csrf_exempt
def tasklist_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    if request.method == 'GET':
        tasks = task_list.task_set.all()
        serializer = SimpleSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializers.errors)