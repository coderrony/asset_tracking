from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Employee, Device, DeviceLog
from .serializer import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
# Create your views here.
# this app you should intaract with api
# you can apply CRDU operation to all model


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def CompnayApi(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Compay add successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        if id is not None:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company,  data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Update Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(
            company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Update data"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        company = Company.objects.get(id=pk)
        company.delete()
        return Response({"msg": "Delete Successfully"})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def EmployeeApi(request, pk=None):
    if request.method == 'GET':
        try:
            id = pk
            if id is not None:
                employee = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(employee)
                return Response(serializer.data)
            employee = Employee.objects.all()
            serializer = EmployeeSerializer(employee, many=True)
            return Response(serializer.data)
        except:
            return Response({"msg": "invalid input"})

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Employee add successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        if id is not None:
            company = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(company,  data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Update Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(
            employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Update data"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            employee = Employee.objects.get(id=pk)
            employee.delete()
            return Response({"msg": "Delete Successfully"})
        except:
            return Response({"msg": "Invalid input"})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def DeviceApi(request, pk=None):
    if request.method == 'GET':
        try:
            id = pk
            if id is not None:
                device = Device.objects.get(id=id)
                serializer = DeviceSerializer(device)
                return Response(serializer.data)
            device = Device.objects.all()
            serializer = DeviceSerializer(device, many=True)
            return Response(serializer.data)
        except:
            return Response({"msg": "invalid input"})

    if request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Device add successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        if id is not None:
            device = Device.objects.get(id=id)
            serializer = DeviceSerializer(device,  data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Update Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        device = Device.objects.get(id=pk)
        serializer = DeviceSerializer(
            device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Update data"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            device = Device.objects.get(id=pk)
            device.delete()
            return Response({"msg": "Delete Successfully"})
        except:
            return Response({"msg": "Invalid input"})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def DeviceLogApi(request, pk=None):
    if request.method == 'GET':
        try:
            id = pk
            if id is not None:
                deviceLog = DeviceLog.objects.get(id=id)
                serializer = DeviceLogSerializer(deviceLog)
                return Response(serializer.data)
            deviceLog = DeviceLog.objects.all()
            serializer = DeviceLogSerializer(deviceLog, many=True)
            return Response(serializer.data)
        except:
            return Response({"msg": "invalid input"})

    if request.method == 'POST':
        serializer = DeviceLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "DeviceLog add successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        if id is not None:
            deviceLog = DeviceLog.objects.get(id=id)
            serializer = DeviceLogSerializer(deviceLog,  data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Update Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        device = DeviceLog.objects.get(id=pk)
        serializer = DeviceLogSerializer(
            device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Update data"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            device = DeviceLog.objects.get(id=pk)
            device.delete()
            return Response({"msg": "Delete Successfully"})
        except:
            return Response({"msg": "Invalid input"})
