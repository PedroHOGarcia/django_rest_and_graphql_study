from django.urls import path

from .views import EmployeeAPIView

urlpatterns = [
    path('v1/employee', EmployeeAPIView.as_view(), name='employee'),
]