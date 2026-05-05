from rest_framework import serializers
from .models import News

class NewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title" , "author" , "content" , "category" , "time" , "views" , "image"]


class NewsListCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id","title" , "author" , "content" , "category" ,"image"]




        