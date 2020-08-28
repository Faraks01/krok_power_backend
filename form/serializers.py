from rest_framework import serializers
from .models import *


class FeedbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = '__all__'


class BillingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingForm
        fields = '__all__'


class BodyShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyShape
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class WireTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WireType
        fields = '__all__'


class WireLengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = WireLength
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
