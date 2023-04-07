from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompnayApi),
    path('<int:pk>/', views.CompnayApi),

    path('employee/', views.EmployeeApi),
    path('employee/<int:pk>/', views.EmployeeApi),

    path('device/', views.DeviceApi),
    path('device/<int:pk>/', views.DeviceApi),

    path('deviceLog/', views.DeviceLogApi),
    path('deviceLog/<int:pk>/', views.DeviceLogApi),
]
