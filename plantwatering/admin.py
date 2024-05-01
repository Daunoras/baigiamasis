from django.contrib import admin
from .models import Plant

class PlantAdmin(admin.ModelAdmin):
    list_display = ('sciname', 'watering', 'name', 'owner', 'watered')

admin.site.register(Plant, PlantAdmin)
