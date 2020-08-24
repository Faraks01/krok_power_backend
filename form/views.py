from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *


class FeedbackFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all().order_by('created')
    serializer_class = FeedbackFormSerializer
    permission_classes = [permissions.AllowAny]


class BillingFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all().order_by('created')
    serializer_class = FeedbackFormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
