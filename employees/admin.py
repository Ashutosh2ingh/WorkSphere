from django.contrib import admin
from .models import Employee, Department, Designation


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'department', 'designation', 'is_active')
    list_filter = ('department', 'designation', 'is_active')
    search_fields = ('employee_id', 'user__username')