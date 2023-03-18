from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views




router = DefaultRouter()

router.register("app_user", views.app_user_modelviewset, basename="app user")
router.register("note", views.note_viewset, basename="note")
router.register("task", views.task_viewset, basename="task")


urlpatterns = [
    path("api_view/", include(router.urls)),
    
]
