from django.urls import path
from . import views

urlpatterns = [
    path('validate-code/<str:code>/', views.validate_code, name='validate_code'),
]
