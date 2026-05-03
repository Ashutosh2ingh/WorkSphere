from django.contrib import admin
from .models import Asset, AssetAllocation


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'asset_type', 'serial_number', 'status')
    list_filter = ('status',)


@admin.register(AssetAllocation)
class AssetAllocationAdmin(admin.ModelAdmin):
    list_display = ('asset', 'employee', 'assigned_date', 'return_date', 'is_active')
    list_filter = ('is_active',)