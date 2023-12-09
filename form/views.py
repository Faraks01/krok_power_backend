from datetime import datetime

from django.core.mail import EmailMessage
from django.http import HttpResponseBadRequest
from rest_framework import permissions
from rest_framework import viewsets

from krok_power_backend.settings import EMAIL_HOST_USER
from view_set_permissions.permissions import CreateOrReadOnly
from .serializers import *


def generate_email_object(title='', message='') -> EmailMessage:
    email = EmailMessage(
        title,
        message,
        EMAIL_HOST_USER,
        [EMAIL_HOST_USER]
    )

    return email


class FeedbackFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all().order_by('created')
    serializer_class = FeedbackFormSerializer
    permission_classes = [CreateOrReadOnly]

    def create(self, request, *args, **kwargs):
        response = super(FeedbackFormViewSet, self).create(request, *args, **kwargs)

        timestamp = datetime.strptime(response.data['created'], "%Y-%m-%dT%H:%M:%S.%fZ")

        message = '''
        Номер заявки: {id}
        Дата создания: {created}
        Номер телефона: {phone_number}
        Имя: {first_name}
        Цвет корпуса: {body_color}
        Backlight: {backlight}
        Золочение шин: {tire_gilding}
        USB порты: {usb_ports}
        Количество розеток: {amount_of_rosette}
        Цвет розеток: {rosette_color}
        Длинна провода: {wire_length}
        Тип корпуса: {body_shape}
        Производитель розеток: {manufacturer}
        Тип провода: {wire_type}
        '''.format(
            id=response.data['id'],
            created=f'{timestamp.date()} {timestamp.hour}:{timestamp.minute}',
            phone_number=response.data['phone_number'],
            first_name=response.data['first_name'],
            body_color=Color.objects.get(pk=response.data['body_color']),
            backlight='✓' if response.data['backlight'] is True else '×',
            tire_gilding='✓' if response.data['tire_gilding'] is True else '×',
            usb_ports='✓' if response.data['usb_ports'] is True else '×',
            amount_of_rosette=response.data['amount_of_rosette'],
            rosette_color=Color.objects.get(pk=response.data['rosette_color']),
            wire_length=WireLength.objects.get(pk=response.data['wire_length']) if response.data[
                                                                                       'wire_length'] is not None else 'Не выбрано',
            body_shape=BodyShape.objects.get(pk=response.data['body_shape']),
            manufacturer=Manufacturer.objects.get(pk=response.data['manufacturer']) if response.data[
                                                                                           'manufacturer'] is not None else 'Не выбрано',
            wire_type=WireType.objects.get(pk=response.data['wire_type']) if response.data[
                                                                                 'wire_type'] is not None else 'Не выбрано',
        )

        email_object = generate_email_object(
            title='Предзаполненная форма обратной связи #{}'.format(response.data['id']),
            message=message
        )

        try:
            email_object.send()
            return response
        except:
            return HttpResponseBadRequest('Failed to send the form')


class BillingFormViewSet(viewsets.ModelViewSet):
    queryset = BillingForm.objects.all().order_by('created')
    serializer_class = BillingFormSerializer
    permission_classes = [CreateOrReadOnly]

    def create(self, request, *args, **kwargs):
        response = super(BillingFormViewSet, self).create(request, *args, **kwargs)

        timestamp = datetime.strptime(response.data['created'], "%Y-%m-%dT%H:%M:%S.%fZ")

        message = '''
        Номер заявки: {id}
        Дата создания: {created}
        Номер телефона: {phone_number}
        Имя: {first_name}
        '''.format(
            id=response.data['id'],
            created=f'{timestamp.date()} {timestamp.hour}:{timestamp.minute}',
            phone_number=response.data['phone_number'],
            first_name=response.data['first_name'],
        )

        email_object = generate_email_object(
            title='Форма обратной связи #{}'.format(response.data['id']),
            message=message
        )

        try:
            email_object.send()
            return response
        except:
            return HttpResponseBadRequest('Failed to send the form')


class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BodyShapeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BodyShape.objects.all()
    serializer_class = BodyShapeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WireTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WireType.objects.all()
    serializer_class = WireTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WireLengthViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WireLength.objects.all()
    serializer_class = WireLengthSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
