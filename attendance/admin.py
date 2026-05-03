from django.contrib import admin
from .models import Attendance, WorkLog


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in', 'check_out', 'status')
    list_filter = ('status', 'date')


@admin.register(WorkLog)
class WorkLogAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'hours_spent')