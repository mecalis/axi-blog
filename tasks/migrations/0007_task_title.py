# Generated by Django 3.1.2 on 2020-10-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20201027_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
