from .serializer import NewsListCreateSerializers , NewsListSerializers
from rest_framework.views import APIView , Response
from rest_framework.generics import RetrieveAPIView , DestroyAPIView , CreateAPIView , UpdateAPIView , ListAPIView,ListCreateAPIView
from .models import News , Likes , User_profile
from rest_framework import viewsets
from rest_framework.decorators import action


class NewsLC(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    
    @action(detail=False ,methods=["get"])
    def Vaqt(self,request):
        news = self.get_queryset().order_by("-id")[:10]
        serializer = self.get_serializer(news , many=True)

        return Response(serializer.data)
    

    @action(detail=True , methods=["post"])

    def Likes_new(self , request,pk=None):
        news = self.get_object()
        user = User_profile.objects.get(user=request.user)
        try:
            like = Likes.objects.create(
                news = news,
                user = user
            )

            return Response(data="like bosildi")

            
        except:

            return Response(data="like bosilmadi")





















