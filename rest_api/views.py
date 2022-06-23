from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ModelViewSet


from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeAPIView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
