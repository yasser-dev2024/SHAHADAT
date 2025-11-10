from django.urls import path
from . import views

urlpatterns = [
    path('validate-code/<str:code>/', views.validate_code, name='validate_code'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
