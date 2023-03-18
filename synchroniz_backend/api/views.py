from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, filters
from .models import *
from .serialiazers import *


import time
from rest_framework.permissions import IsAuthenticated
from datetime import timedelta
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, QueryDict



# Create your views here.

class app_user_modelviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = app_user_serializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['email']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.perform_create(serializer)

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        response_data = {
            'refresh': str(refresh),
            'access': str(access_token),
        }

        headers = self.get_success_headers(serializer.data)
        return Response(response_data, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        return user


class note_viewset(viewsets.ModelViewSet):
    queryset = note.objects.all()
    serializer_class = note_serializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class task_viewset(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = task_serializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class category_viewset(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = category_serializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]