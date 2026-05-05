from django.contrib import admin
from django.urls import path, include
from .views import NewsLC
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Yangi", NewsLC, basename="News")


urlpatterns = [
    path("New" , include(router.urls) , name="New")
]