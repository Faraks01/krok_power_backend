from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NewsSerializer, News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('created')
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]
