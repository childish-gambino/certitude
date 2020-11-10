#-*-coding utf-16-*-
import csv, io
import json
from django.shortcuts import render
from django.contrib import messages
from iaudit.models import HardwareEntitlement, ScanCSV

from rest_framework import generics
from iaudit.serializers import HardwareEntitlementSerializer
from rest_framework import viewsets

from django.db.models import Count, Q
from pprint import pprint
# import codecs from django.utils.encoding
# Create your views here.
# one parameter named request
def user_landed(request):
    template = "index.html"
    data = ScanCSV.objects.all()
    # prompt is a context variable that can have different values depending on their context
    prompt = {'order': 'Only accepts one column that is appname', 'scancsv': data}
    # GET request returns the value of the data with the specified key.
    try:
        just_logged_out = request.session.get('just_logged_out',False)
    except:
        just_logged_out = False
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    filename = ((request.FILES['file'].name)[0:-4])
    if filename.startswith('AUDI-MAC'):
        encoding = 'UTF-8'
    else:
        encoding = 'UTF-16'
    context = {}
    if request.method == "POST":
        try:
            data_set = csv_file.read().decode(encoding)
            # process CSV entries
            io_string = io.StringIO(data_set)
            next(io_string)
            # fo = codecs.open('filename', 'r', 'utf-16')
            # zz = fo.readlines()
            pprint(dir(request.user))
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                _, created = ScanCSV.objects.update_or_create(
                    appname=column[0],
                    email=str(request.user.email),
                    serialnumber=filename,
                )
            messages.success(request, "Uploaded Successfully")
        except Exception as e:
            print("WOOOPS!!!",e)
            messages.warning(request,"THIS IS NOT A CSV FILE")
        return render(request, template, context)


class ListHardwareEntitlement(generics.ListCreateAPIView):
        queryset = HardwareEntitlement.objects.all()
        serializer_class = HardwareEntitlementSerializer

class DetailedHardwareEntitlement(generics.RetrieveUpdateDestroyAPIView):
    queryset = HardwareEntitlement.objects.all().order_by('id')
    serializer_class = HardwareEntitlementSerializer


