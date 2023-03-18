from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, filters
from .models import *
from .serialiazers import *

# Create your views here.

class app_user_modelviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = app_user_serializer
    

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        return user


class note_viewset(viewsets.ModelViewSet):
    queryset = note.objects.all()
    serializer_class = note_serializer
   


class task_viewset(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = task_serializer
    


class category_viewset(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = category_serializer
    
