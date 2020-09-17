import csv, io
from django.shortcuts import render
from django.contrib import messages
from iaudit.models import ScanCSV

# Create your views here.
# one parameter named request
def scancsv_upload(request):
    # declaring template
    template = "index.html"
    data = ScanCSV.objects.all()
# prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Only accepts one column that is appname',
        'scancsv': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = ScanCSV.objects.update_or_create(
            appname=column[0],
            # email=column[1],
        )
    context = {
        "errors": "Woops!",
        "success": "Uploaded Successfully"
        }
    return render(request, template, context)