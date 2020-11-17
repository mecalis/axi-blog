from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from .models import Task,Task2, Task3, TaskListModel, TaskListModel2, TaskListModel3
from .forms import TaskForm, TaskListModel3Form, Task3ModelForm, Task3Form

# Create your views here.
def index(request):

    list = TaskListModel.objects.all()[0]

    tasks = Task.objects.all()
    form = TaskForm()


    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(index)

    context = {'tasks': tasks, 'form': form, 'list': list}
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
    item = Task3.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect(index2)

    return render(request, 'tasks/delete.html', context)

def index2(request):
    user = request.user
    #print('user:', user)
    tasklistnames = TaskListModel3.objects.filter(owner=user) | TaskListModel3.objects.filter(shared__contains=user)
    # print('Listák nevei:',tasklistnames)
    # print('\n-------------')

    tasks_by_lists = []
    list = []
    for tasklistname in tasklistnames:
        tasklistnametitle = str(tasklistname.list_title)
        #print('Tasklista neve:', tasklistname, 'elemei:\n')
        task_in_list = Task3.objects.filter(tasklist__list_title__iexact=tasklistnametitle)
        #print(str(task_in_list.query), '\n')
        sublist = [tasklistname, task_in_list]
        tasks_by_lists.append(sublist)

    form = TaskListModel3Form()

    if request.method == 'POST':
        #print('POST')
        #print('POST user:', request.user)
        form = TaskListModel3Form(request.POST)

        if form.is_valid():
            #print('valid? valid')
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()

        return redirect(index2)

    context = {'form': form, 'tasks_by_lists' : tasks_by_lists}
    return render(request, 'tasks/list2.html', context)

def list_detail(request, pk):
    list = TaskListModel3.objects.get(id=pk)
    list_title = list.list_title
    #print('A küldött list:', list)

    if request.method == 'POST':

        title = request.POST.get("task_title")
        if title:
            task = Task3()
            task.tasklist = list
            task.task_title = title

            task.save()
    # if request.method == 'POST':
    #     form = Task3ModelForm(request.POST)
    #
    #     print('task title a formban:',form["task_title"].value())
    #     print('task to list', form["tasklist"].value())
    #     #form.data['tasklist'] = list
    #     #form.tasklist = request.POST.get("tasklist")
    #     if form.is_valid():
    #         print('VALID')
    #         form.save()

    form = Task3ModelForm()

    tasks_in_list = Task3.objects.filter(tasklist__list_title__iexact=list_title)
    #print('A küldött tasks_in_list:', tasks_in_list)

    context = {'tasks_in_list': tasks_in_list, 'list': list, 'form': form}
    return render(request, 'tasks/listdetail.html', context)

def delete_list(request, pk):
    list = TaskListModel3.objects.get(id=pk)

    list.delete()
    return redirect(index2)

def taskupdate(request, pk):
    task = Task3.objects.get(id=pk)
    form = Task3Form(instance=task)
    print('pk=', pk)
    if request.method == 'POST':
        form = Task3Form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(index2)

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

def tasktoggle(request, pk):
    list_id = request.POST.get('list_id')
    if request.method == 'POST':
        task = Task3.objects.get(pk=pk)
        if task.complete == True:
            print('Task complete', task.complete)
            task.complete = False
            task.save()
        else:
            task.complete = True
            task.save()
            print('Task complete', task.complete)
    return redirect(list_detail, pk = list_id)

def updateList(request, pk):
    list = TaskListModel3.objects.get(id=pk)
    form = TaskListModel3Form(instance=list)

    if request.method == 'POST':
        form = TaskListModel3Form(request.POST, instance=list)
        if form.is_valid():
            form.save()
            list_id = list.id
            return redirect(list_detail, pk = list_id)

    context = {'form': form}
    return render(request, 'tasks/update_list.html', context)



