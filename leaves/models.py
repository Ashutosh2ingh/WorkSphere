from django.db import models
from core.models import BaseModel


class Leave(BaseModel):
    LEAVE_TYPE = (
        ('casual', 'Casual'),
        ('sick', 'Sick'),
        ('paid', 'Paid'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)

    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE)

    start_date = models.DateField()
    end_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    approved_by = models.ForeignKey(
        'employees.Employee',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='approved_leaves'
    )