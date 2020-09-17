import csv, io
from django.shortcuts import render
from django.contrib import messages
from iaudit.models import ScanCSV

# Create your views here.
# one parameter named request
def scancsv_upload(request):
    template = "index.html"
    data = ScanCSV.objects.all()
# prompt is a context variable that can have different values depending on their context
    prompt = {'order': 'Only accepts one column that is appname', 'scancsv': data}
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    context = {}

    if request.method == "POST":
        try:
            data_set = csv_file.read().decode('UTF-8')
            # process CSV entries
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                _, created = ScanCSV.objects.update_or_create(
                    appname=column[0],
                    email=str(request.user.email),
                )
            messages.success(request, "Uploaded Successfully")
        except Exception as e:
            print(e)
            messages.warning(request,"THIS IS NOT A CSV FILE")
        return render(request, template, context)
