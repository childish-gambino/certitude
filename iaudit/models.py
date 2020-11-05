from django.db import models


class ScanCSV(models.Model):
    appname = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    serialnumber = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.appname

