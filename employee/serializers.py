from .models import Department, Employee
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.CharField(source='department.name')
    
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department', )