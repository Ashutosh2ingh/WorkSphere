from django.db import models
from core.models import BaseModel


class Salary(BaseModel):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)

    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    month = models.IntegerField()
    year = models.IntegerField()

    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)