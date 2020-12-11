from django.db import models

# Create your models here.
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.conf import settings

class Materials(models.Model):
    name = models.CharField(max_length=200)
    unit_type = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Ingredient(models.Model):
    title3 = models.CharField(max_length=200, null=True, blank=True)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE)
    quantity = models.FloatField()
    note = models.CharField(max_length=200, null=True, blank=True)



""""
class Recipe(models.Model):
    parts = models.ManyToManyField(Part)

    def __str__(self):
        return str(self.name)

class Warehouse(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    parts = models.ManyToManyField(Part)

    def __str__(self):
        return str(self.name)

"""