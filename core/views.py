from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from core.constants import DynamicVariables
from .models import Category
from .serializers import CategorySerializer

class DynamicVariablesView(APIView):
    """
    Exposes the list of dynamic variables as an API endpoint
    """
    def get(self, request):
        variables = [var.value for var in DynamicVariables]
        return Response({"variables": variables})
