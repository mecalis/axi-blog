from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Materials)

# admin.site.register(Recipe)
# admin.site.register(Warehouse)