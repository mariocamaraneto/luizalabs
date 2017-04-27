from .models import Department, Employee
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name')
    
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department', )
        
    def create(self, validated_data):
        """
        Cria e retorna uma nova instacia de Employee
        """
        department, _ = Department.objects.get_or_create(name=validated_data['department']['name'])
        validated_data['department'] = department
        
        return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Atualiza e retorna uma nova instacia de Employee
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        
        departmentName = validated_data.get('department', {}).get('name', instance.department.name)
        instance.department, _ = Department.objects.get_or_create(name=departmentName)
        
        instance.save()
        return instance
    