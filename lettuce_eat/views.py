from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets
from .models import Restaurant
from .permissions import IsAuthorOrReadOnly
from .serializers import RestaurantSerializer, UserSerializer

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer