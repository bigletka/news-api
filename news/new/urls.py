from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from new import views




urlpatterns = [
    path('list/', views.NewsList.as_view(), name='list')
]
