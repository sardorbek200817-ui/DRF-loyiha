from django.shortcuts import render
from rest_framework import serializers
from .serializer import ProductSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView , DestroyAPIView , CreateAPIView , UpdateAPIView , ListAPIView
from .models import Product


class ProductDestroy(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieve(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdate(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
