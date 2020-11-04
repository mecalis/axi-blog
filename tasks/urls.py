from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index_page2'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete_task'),
    path('delete2/<str:pk>/', views.deleteTask2, name='delete_task2'),
    path('list_detail/<str:pk>/', views.list_detail, name='list_detail'),
]