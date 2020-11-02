from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from .models import Task,Task2, TaskListModel, TaskListModel2
from .forms import TaskForm

# Create your views here.
def index(request):

    tasklistnames = TaskListModel2.objects.all()
    print('Tasklisták nevei:', tasklistnames)
    tasks_by_lists = []
    list = []
    for tasklistname in tasklistnames:

        task_in_list = Task2.objects.filter(tasklistmodel2__list_title__contains=tasklistname)
        sublist=[tasklistname, task_in_list]

        tasks_by_lists.append(sublist)
    print('tasks_by_lists', tasks_by_lists)

    tasks = Task.objects.all()
    form = TaskForm()


    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(index)

    context = {'tasks': tasks, 'form': form,'tasks_by_lists':tasks_by_lists}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(index)

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect(index)

    return render(request, 'tasks/delete.html', context)

def deleteTask2(request, pk):
    item = Task2.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect(index)

    return render(request, 'tasks/delete.html', context)

