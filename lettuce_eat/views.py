from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Restaurant
from .permissions import IsAuthorOrReadOnly
from .serializers import RestaurantSerializer, UserSerializer

# Create your views here.
class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer