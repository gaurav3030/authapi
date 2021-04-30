from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json
from faceauth.Train import *
from faceauth.Recognize import *
from voiceauth.register import *
from voiceauth.login import *
import cv2 
@csrf_exempt
# Create your views here.
def index(request):
    if request.method == 'POST':
        content = request.POST
        uploadedfile = request.FILES['face']
        fs = FileSystemStorage()
        savedfile = fs.save(uploadedfile.name,uploadedfile)

        username =content['name']
        videopath = "dataset\\"+savedfile
        print(videopath)
        trainface_v(videopath,username)
    return HttpResponse("Registeration done for face")
@csrf_exempt
def facelogin(request):
    if request.method == 'POST':
        location="dataset\\loginspace"
        content = request.POST
        facefile = request.FILES['face']
        voicefile = request.FILES['voice']
        fs = FileSystemStorage(location)
        savedfacefile = fs.save(facefile.name,facefile)
        savedvoicefile = fs.save(voicefile.name,voicefile)
        otp =content['otp']
        
        facepath = "dataset\\loginspace\\"+savedfacefile
        voicepath = "dataset\\loginspace\\"+savedvoicefile

        predictedface = recognize_face(facepath)
        predictedvoicename = recognize_voice(otp,voicepath,predictedface[1])
    return HttpResponse(predictedvoicename)


@csrf_exempt
def voiceregister(request):
    if request.method == 'POST':
        content = request.POST
        name =content['name']
        location="dataset\\voice\\"+name
        uploadedfiles = request.FILES
        fs = FileSystemStorage(location=location)
        
        count =0
        for files in uploadedfiles:
            
            trainedfilelist = open("training_file.txt", 'a')
            OUTPUT_FILENAME = str(count) + "_" + name + "_1.wav"
            trainedfilelist.write(OUTPUT_FILENAME+"\n")
            savedfile = fs.save(OUTPUT_FILENAME,uploadedfiles[files])
            trainedfilelist.close()
            count+=1
        registervoice(name)

        
        


    return HttpResponse("registration done for voice")

@csrf_exempt
def voicelogin(request):
    if request.method == 'POST':
        content = request.POST
        name =content['name']
        location="dataset\\voice\\"+name


        
        


    return HttpResponse("True")