from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('task_list/', views.task_list_list),
    path('task_list/<int:pk>/',views.task_list_detail),
    path('task_list/<int:pk>/task',views.task_list),
    path('tasks/<int:pk>/',views.task_detail)
]
