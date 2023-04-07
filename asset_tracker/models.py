from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Device(models.Model):
    current_condition = (
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    )
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=30, unique=True)
    condition = models.CharField(
        choices=current_condition, max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    current_condition = (
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField(default=timezone.now)
    check_in_time = models.DateTimeField(blank=True, null=True)
    check_out_condition = models.CharField(
        max_length=100, blank=True, choices=current_condition)
    check_in_condition = models.CharField(
        max_length=100, blank=True, choices=current_condition)
