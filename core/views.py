from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from core.constants import DynamicVariables
from .models import Category, EmailTemplate
from .serializers import CategorySerializer, EmailTemplateSerializer

class DynamicVariablesView(APIView):
    """
    Exposes the list of dynamic variables as an API endpoint
    """
    def get(self, request):
        variables = [var.value for var in DynamicVariables]
        return Response({"variables": variables})

#   ViewSets for CRUD operations 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer