from django.db import models


class ScanCSV(models.Model):
    appname = models.TextField()
    email = models.EmailField(blank=True)
    def __str__(self):
        return self.name