from django.shortcuts import render
from rest_framework import (
    viewsets,
    mixins,
    status,
 )

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from new import serializers
from core.models import News
from rest_framework.views import APIView
from rest_framework import generics
from new.serializers import NewsSerializers

# Create your views here.


class NewsList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
