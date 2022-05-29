from rest_framework import serializers
from .models import *


class Feedserializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPost
        fields = '__all__'


class Bannerserializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
