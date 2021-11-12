from django.urls import path
from .views import RestaurantList, RestaurantDetail, UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('', RestaurantList.as_view()),
    path('<int:pk>', RestaurantDetail.as_view())
]