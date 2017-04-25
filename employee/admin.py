from django.contrib import admin
from .models import Employee, Department

admin.site.site_header = 'Employee Manager'


# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
