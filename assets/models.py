from django.db import models
from core.models import BaseModel


class Asset(BaseModel):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('assigned', 'Assigned'),
        ('repair', 'Repair'),
    )

    name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100, unique=True)

    purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class AssetAllocation(BaseModel):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)

    assigned_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)