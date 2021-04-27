from django.urls import path

from . import views

urlpatterns = [
    path('regface/', views.index, name='index'),
    path('logface/', views.facelogin, name='facelogin'),
    path('regvoice/', views.voiceregister, name='voiceregister'),
    path('logvoice/', views.voicelogin, name='voicelogin'),
    
]