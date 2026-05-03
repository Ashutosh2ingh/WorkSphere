from django.contrib import admin
from .models import Performance


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'rating', 'review_period', 'created_at')
    list_filter = ('rating',)