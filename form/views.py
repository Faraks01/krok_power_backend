from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from django.core.mail import EmailMessage


def send_email(serializer):
    email = EmailMessage(
        'Title',
        serializer.fields,
        'my-email',
        ['my-receive-email']
    )
    email.send()


class FeedbackFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all().order_by('created')
    serializer_class = FeedbackFormSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super(FeedbackFormViewSet, self).create(request, *args, **kwargs)
        send_email(FeedbackFormSerializer)  # sending mail
        return response


class BillingFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all().order_by('created')
    serializer_class = FeedbackFormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        response = super(BillingFormViewSet, self).create(request, *args, **kwargs)
        send_email(FeedbackFormSerializer)  # sending mail
        return response
