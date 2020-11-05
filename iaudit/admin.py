from django.contrib import admin

# Register your models here.
from .models import ScanCSV

def download_csv(modeladmin, request, queryset):
    import csv
    f = open('some.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["email", "appname", "serialnumber"])
    for s in queryset:
        writer.writerow([s.email, s.appname, s.serialnumber])

class ScannedMachines(admin.ModelAdmin):
    list_display = [field.name for field in ScanCSV._meta.get_fields()]
    list_filter = ['appname','email']
    search_fields = ('appname', 'email', 'serialnumber' )
    actions = [download_csv]



admin.site.register(ScanCSV,ScannedMachines)


# @admin.register(ScanCSV)
# class AudiDash(admin.ModelAdmin):
#     change_list_template = 'audidash.html'