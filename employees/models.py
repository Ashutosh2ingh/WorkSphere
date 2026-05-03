from django.db import models
from core.models import BaseModel


class Department(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Designation(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(BaseModel):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)

    employee_id = models.CharField(max_length=20, unique=True)

    phone = models.CharField(max_length=15)
    address = models.TextField()

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)

    joining_date = models.DateField()
    employment_type = models.CharField(max_length=50)

    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} ({self.employee_id})"