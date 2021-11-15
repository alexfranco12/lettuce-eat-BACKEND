from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, RestaurantViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('restaurants', RestaurantViewSet, basename='restaurants')

urlpatterns = [

]


urlpatterns += router.urls