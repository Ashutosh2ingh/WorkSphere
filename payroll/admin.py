from django.contrib import admin
from .models import Salary


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'year', 'net_salary', 'is_paid')
    list_filter = ('is_paid', 'month', 'year')