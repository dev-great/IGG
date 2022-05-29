from rest_framework import serializers
from .models import *


class Notificationserializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPost
        fields = '__all__'
