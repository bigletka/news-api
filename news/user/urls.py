from django.urls import path

from user import views
from rest_framework_simplejwt import views as jwt_views


app_name ='user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    #  path('token/refresh/', 
    #       jwt_views.TokenRefreshView.as_view(), 
    #       name ='token_refresh'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]