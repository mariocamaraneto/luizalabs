from django.db import models

# Create your models here.

class Department (models.Model):
    """
    Resposável por classificar os empregados (Employee)
    TODO: Armazenar qual usuário criou e modificou o grupo
    """
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def _str__(self):
        return self.name


class Employee (models.Model):
    """
    Resposável por guardar as informações dos empregados
    TODO: Armazenar qual usuário criou e modificou o grupo
    """
    name = models.CharField(max_length=120)
    email = models.EmailField()
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
