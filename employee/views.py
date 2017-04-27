from .models import Department, Employee
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Classe que retorna requisições REST da entidade Employee
    Operações aceitas: listagem, recuperação de registro, criação, atualização e remoção.
    Ref: http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    """
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer

class DepartmentViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """
    Classe que retorna requisições REST da entidade Department
    Operações aceitas: listagem e recuperação de um registro.
        Função de criação desabilitado julgando que todos departamentos serão
        criados dinâmicamente conforme adiciona-se novos Employees.
    Ref: http://www.django-rest-framework.org/api-guide/viewsets/#custom-viewset-base-classes
    """    
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer