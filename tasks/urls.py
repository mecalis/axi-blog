from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index_page2'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete_task'),
    path('delete2/<str:pk>/', views.deleteTask2, name='delete_task2'),
    path('delete_list/<str:pk>/', views.delete_list, name='delete_list'),
    path('list_detail/<str:pk>/', views.list_detail, name='list_detail'),
    path('taskupdate/<str:pk>/', views.taskupdate, name='taskupdate'),
    path('tasktoggle/<str:pk>/', views.tasktoggle, name='tasktoggle'),
    path('update_list/<str:pk>/', views.updateList, name='update_list'),
    path('list_clear/<str:pk>/', views.list_clear, name='list_clear'),
]