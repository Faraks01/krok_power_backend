from rest_framework import serializers
from .models import FeedbackForm, BillingForm


class FeedbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = '__all__'


class BillingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingForm
        fields = '__all__'
