from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('<str:username>/repositories/', views.userRepositories, name='user-repositories'),
    path('<str:username>/sum-of-stars/', views.userSumOfStars, name='user-stars'),
]
