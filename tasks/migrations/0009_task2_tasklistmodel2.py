# Generated by Django 3.1.2 on 2020-10-29 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_auto_20201027_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(blank=True, max_length=200, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskListModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared', models.CharField(blank=True, max_length=200, null=True)),
                ('list_title', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ManyToManyField(to='tasks.Task2')),
            ],
        ),
    ]