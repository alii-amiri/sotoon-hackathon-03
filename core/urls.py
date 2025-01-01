from django.urls import path
from .views import DynamicVariablesView

urlpatterns = [
    path('dynamic-variables/', DynamicVariablesView.as_view(), name='dynamic-variables'),
]
