from rest_framework import mixins, status, serializers,generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response


class ListCreateApiView(generics.ListAPIView,
                        generics.CreateAPIView):
    queryset = Employee.objects.all().order_by('age')
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        employee = serializer.save()
        print(f"Created new Employee: name: {employee.name}, email: {employee.email}, age: {employee.age}")


class RetriveUpdateDestroyApiView(generics.RetrieveAPIView,
                                  generics.UpdateAPIView,
                                  generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_destroy(self, instance):
        instance.archived = True
        instance.save()
