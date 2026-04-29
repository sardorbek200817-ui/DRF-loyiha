from django.contrib import admin
from django.urls import path, include
from .views import ProductCreate  ,ProductDestroy , ProductRetrieve , ProductUpdate , ProductList

urlpatterns = [
    path("Update/<int:pk>" , ProductUpdate.as_view()),
    path("Destroy/<int:pk>" , ProductDestroy.as_view()),
    path("Create" , ProductCreate.as_view()),
    path("Retrieve/<int:pk>" , ProductRetrieve.as_view()),
    path("List" , ProductList.as_view()),
]
