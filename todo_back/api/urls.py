from django.contrib import admin
from django.urls import path, include
from .views import task_list, task_list_detail

urlpatterns = [
    path('task_list/', task_list),
    path('task_list/<int:pk>/',task_list_detail),
    # path('task_list/<int:pk>/task',views.task_list),
    # path('tasks/<int:pk>/',views.task_detail)
]
