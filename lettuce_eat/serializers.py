from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

  class Meta:
    model = Restaurant
    fields = ('id', 'name', 'summary', 'website', 'image_url',)


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = get_user_model()
    fields = ('id', 'username',)