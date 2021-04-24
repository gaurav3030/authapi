from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json
from faceauth.Train import *
import cv2 
@csrf_exempt
# Create your views here.
def index(request):
    if request.method == 'POST':
        content = request.POST
        uploadedfile = request.FILES['face']
        fs = FileSystemStorage()
        savedfile = fs.save(uploadedfile.name,uploadedfile)
        # face_cascade = './Haar_Cascades/haarcascade_frontalface_default.xml'
        # right_eye_cascade = './Haar_Cascades/haarcascade_righteye_2splits.xml'
        # left_eye_cascade = './Haar_Cascades/haarcascade_lefteye_2splits.xml'
        # radius = 1
        # neighbour = 8
        # grid_x = 8
        # grid_y = 8
        # var = list([radius,neighbour,grid_x,grid_y])
        # modelface = Train_Model(face_cascade,right_eye_cascade,left_eye_cascade,var)
        username =content['name']
        videopath = "dataset\\"+savedfile
        print(videopath)
        trainface_v(videopath,username)
    return HttpResponse("Hello, world. You're at the polls index.")