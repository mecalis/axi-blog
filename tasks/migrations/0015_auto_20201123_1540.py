# Generated by Django 3.1.2 on 2020-11-23 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_auto_20201105_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task3',
            options={'ordering': ['-created']},
        ),
    ]
