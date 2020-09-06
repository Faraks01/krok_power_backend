from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from .serializers import NewsSerializer, News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created']
