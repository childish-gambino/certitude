from django.db import models


class ScanCSV(models.Model):
    appname = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    serialnumber = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.appname

class HardwareEntitlement(models.Model):
    uuid = models.TextField(blank=False,unique=True)
    email = models.EmailField(blank=False)
    hardware_serial = models.CharField(max_length=50,blank=True)
    computer_name = models.CharField(max_length=255,blank=True)
    hostname = models.CharField(max_length=255,blank=True)
    status = models.CharField(max_length=5,blank=False)
    def __str__(self):
        return self.appname

