from django.contrib import admin
from django.urls import path, include
from .views import NewsLC , Sen , U , NewLCView111
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("Yangi", NewsLC, basename="News")



router1 = DefaultRouter()
router1.register("U" , NewLCView111 , basename="U")


urlpatterns = [
    path("New" , include(router.urls) , name="New"),
    path("Sen/<int:pk>" , Sen.as_view()),
    path("uv" , include(router1.urls)),
]











