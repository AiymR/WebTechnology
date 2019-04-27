from django.contrib import admin
from django.urls import path, include
from .views import tasklist_detail,todo_detail,task_list,tasklist_task

urlpatterns = [
    path('task_list/', task_list),
    path('task_list/<int:pk>/',tasklist_detail),
    path('task_list/<int:pk>/task/',tasklist_task),
    path('tasks/<int:pk>/',todo_detail)
]
