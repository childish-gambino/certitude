from django.contrib import admin

# Register your models here.
from .models import ScanCSV

class ScannedMachines(admin.ModelAdmin):
    list_display = [field.name for field in ScanCSV._meta.get_fields()]
admin.site.register(ScanCSV,ScannedMachines)
