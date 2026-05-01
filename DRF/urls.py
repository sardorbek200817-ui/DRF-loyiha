from django.contrib import admin
from django.urls import path, include
from .views import NewsListCreateViews


urlpatterns = [
    path("New" , NewsListCreateViews.as_view() , name="New")
]