from .serializer import NewsListCreateSerializers , NewsListSerializers
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView , DestroyAPIView , CreateAPIView , UpdateAPIView , ListAPIView,ListCreateAPIView
from .models import News



class NewsListCreateViews(ListCreateAPIView):
        queryset = News.objects.all()

        def get_serializer_class(self):
            if self.request.method == "POST":
                return NewsListCreateSerializers
            return NewsListSerializers


    

    


