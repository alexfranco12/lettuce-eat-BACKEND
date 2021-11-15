from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets, permissions
from .models import Restaurant
from .permissions import IsAuthorOrReadOnly, ReadOnly
from .serializers import RestaurantSerializer, UserSerializer

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = (ReadOnly,)
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer