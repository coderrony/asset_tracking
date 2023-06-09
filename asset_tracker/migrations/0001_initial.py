# Generated by Django 4.2 on 2023-04-06 14:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=30, unique=True)),
                ('condition', models.CharField(choices=[('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=100)),
                ('is_available', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_tracker.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_tracker.company')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('check_in_time', models.DateTimeField(blank=True, null=True)),
                ('check_out_condition', models.CharField(blank=True, choices=[('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=100)),
                ('check_in_condition', models.CharField(blank=True, choices=[('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_tracker.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_tracker.employee')),
            ],
        ),
    ]
