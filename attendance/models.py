from django.db import models
from core.models import BaseModel


class Attendance(BaseModel):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('half_day', 'Half Day'),
        ('leave', 'Leave'),
    )

    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    date = models.DateField()

    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)

    total_hours = models.FloatField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('employee', 'date')


class WorkLog(BaseModel):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    date = models.DateField()

    task_description = models.TextField()
    hours_spent = models.FloatField()