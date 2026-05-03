from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Notification(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)


class AuditLog(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    model_name = models.CharField(max_length=100)