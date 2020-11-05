from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from .models import Task,Task2, Task3, TaskListModel, TaskListModel2, TaskListModel3
from .forms import TaskForm, TaskListModel3Form, Task3Form

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

def index2(request):
    tasklistnames = TaskListModel3.objects.all()
    print('Listák nevei:',tasklistnames)
    print('\n-------------')

    tasks_by_lists = []
    list = []
    for tasklistname in tasklistnames:
        print('Tasklista neve:', tasklistname, 'elemei:\n')
        task_in_list = Task3.objects.filter(tasklist__list_title__iexact=tasklistname)
        print(task_in_list, '\n')
        sublist = [tasklistname, task_in_list]
        tasks_by_lists.append(sublist)

    form = TaskListModel3Form()

    if request.method == 'POST':
        print('POST')
        print('POST user:', request.user)
        form = TaskListModel3Form(request.POST)

        if form.is_valid():
            print('valid? valid')
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()

        return redirect(index2)

    context = {'form': form, 'tasks_by_lists' : tasks_by_lists}
    return render(request, 'tasks/list2.html', context)

def list_detail(request, pk):
    list = TaskListModel3.objects.get(id=pk)
    print('A küldött list:', list)

    if request.method == 'POST':
        title = request.POST.get("task_title")
        if title:
            task = Task3()
            task.tasklist = list
            task.task_title = title

            task.save()


    form = Task3Form()

    tasks_in_list = Task3.objects.filter(tasklist__list_title__iexact=list)
    #print('A küldött tasks_in_list:', tasks_in_list)

    context = {'tasks_in_list': tasks_in_list, 'list': list, 'form': form}
    return render(request, 'tasks/listdetail.html', context)
