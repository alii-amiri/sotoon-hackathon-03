from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DynamicVariablesView, CategoryViewSet, EmailTemplateViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'templates', EmailTemplateViewSet, basename='template')

urlpatterns = [
    path('dynamic-variables/', DynamicVariablesView.as_view(), name='dynamic-variables'),
    path('', include(router.urls)),
]
