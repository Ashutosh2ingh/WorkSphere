from django.db import models
from core.models import BaseModel


class Performance(BaseModel):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)

    review_period = models.CharField(max_length=50)
    rating = models.IntegerField()
    feedback = models.TextField()

    reviewed_by = models.ForeignKey(
        'employees.Employee',
        related_name='reviews_given',
        on_delete=models.SET_NULL,
        null=True
    )