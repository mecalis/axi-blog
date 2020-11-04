from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#User = settings.AUTH_USER_MODEL


# Create your models here.
class TaskListModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    shared = models.CharField(max_length=200, null=True, blank=True)
    list_title = models.CharField(max_length=200)

    def __str__(self):
        return str(self.owner) + ' - ' + str(self.list_title)

class Task(models.Model):
    tasklist = models.ForeignKey(TaskListModel, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.task_title) + ' on ' + str(self.tasklist)

class Task2(models.Model):
    task_title = models.CharField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.task_title)

class TaskListModel2(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    shared = models.CharField(max_length=200, null=True, blank=True)
    task = models.ManyToManyField(Task2, null=True, blank=True)
    list_title = models.CharField(max_length=200)

    def __str__(self):
        return str(self.list_title)

class TaskListModel3(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    shared = models.CharField(max_length=200, null=True, blank=True)
    list_title = models.CharField(max_length=200)

    def __str__(self):
        return self.list_title

class Task3(models.Model):
    tasklist = models.ForeignKey(TaskListModel3, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title