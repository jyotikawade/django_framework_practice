"""
whatever model we create we need to register them over here
"""


from django.contrib import admin
from employees.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']
    """this fields will be displayed in admin panel"""


admin.site.register(Employee, EmployeeAdmin)
