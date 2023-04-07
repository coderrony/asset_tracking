from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog
# Register your models here.


admin.site.register(Company)


@admin.register(Employee)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'email', 'company']
    ordering = ('-name',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'serial_number',
                    'condition', 'company', 'is_available']
    ordering = ('-name',)


@admin.register(DeviceLog)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'id', 'device',
                    'check_out_time', 'check_in_time', 'check_out_condition', 'check_in_condition']
