from django.contrib import admin
from django.urls import path, include
from .views import tasklist_detail,tasklist_list,todo_detail,todo_list,task_list,detailed_task_list,tasks_list,tasklist_tasks

urlpatterns = [
    path('task_list/', task_list),
    path('task_list/<int:pk>/',tasklist_detail),
    path('task_list/<int:pk>/task',tasklist_tasks),
    path('tasks/<int:pk>/',todo_detail)
]
