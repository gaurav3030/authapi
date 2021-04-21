from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json

@csrf_exempt
# Create your views here.
def index(request):
    if request.method == 'POST':
        body_unicode = request.body
       
        content = body_unicode['name']
        uploadedfile = request.FILES['face']
        fs = FileSystemStorage()
        savedfile = fs.save(uploadedfile.name,uploadedfile)
        
        print(content)
    return HttpResponse("Hello, world. You're at the polls index.")