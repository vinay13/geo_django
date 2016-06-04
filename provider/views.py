from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from provider.models import Providers,ServiceArea
from provider.serializers import ProviderSerializer,ServiceAreaSerializer
from rest_framework import filters,viewsets






class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Providers.objects.all()
    serializer_class = ProviderSerializer



class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer