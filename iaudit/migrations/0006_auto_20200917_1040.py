# Generated by Django 3.1.1 on 2020-09-17 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iaudit', '0005_auto_20200916_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='scancsv',
            name='serialnumber',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='scancsv',
            name='appname',
            field=models.TextField(blank=True),
        ),
    ]