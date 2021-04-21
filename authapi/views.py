from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json

@csrf_exempt
# Create your views here.
def index(request):
    if request.method == 'POST':
        content = request.POST
        uploadedfile = request.FILES['face']
        fs = FileSystemStorage()
        savedfile = fs.save(uploadedfile.name,uploadedfile)
        
        print(content['name'])
    return HttpResponse("Hello, world. You're at the polls index.")