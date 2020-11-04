#
# # Create your models here.
# class TaskListModel(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
#     shared = models.CharField(max_length=200, null=True, blank=True)
#     list_title = models.CharField(max_length=200)
#
#     def __str__(self):
#         return str(self.owner) + ' - ' + str(self.list_title)
#
# class Task(models.Model):
#     tasklist = models.ForeignKey(TaskListModel, on_delete=models.CASCADE)
#     task_title = models.CharField(max_length=200, null=True, blank=True)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.task_title) + ' on ' + str(self.tasklist)