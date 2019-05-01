from django.urls import path
from api import views

# urlpatterns = [
#     path('task_list/', views.tasklist_list),
#     # path('task_list/<int:pk>/',views.tasklist_detail),
#     # path('task_list/<int:pk>/task/',views.tasklist_task),
#     # path('tasks/<int:pk>/',views.todo_detail)
# ]
urlpatterns = [
    path('task_list/', views.TaskListList.as_view()),
    path('task_list/<int:pk>/',views.TaskListCrud.as_view()),
    path('task_list/<int:pk>/task/',views.tasks_list),
    path('tasks/<int:pk>/',views.Task_Detail.as_view()),
    path('users/',views.UserList.as_view()),
    path('login/',views.login),
    path('logout/',views.logout),
]
