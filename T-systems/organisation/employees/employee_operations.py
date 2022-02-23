from .models import Employee
from .serializers import EmployeeSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework import status


def DisplayEmployee(id):
    if id is not None:
        try:
            specific_employee_obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            s_status = status.HTTP_404_NOT_FOUND
            return s_status
        else:
            serializer = EmployeeSerializer(specific_employee_obj)
            return serializer.data

    all_employee_obj = Employee.objects.all()
    serializer = EmployeeSerializer(all_employee_obj, many=True)  # if multiple object then many = true
    return serializer.data


def CreateEmployee(request):
    json_data = request.body  # getting json data and converting to python
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = EmployeeSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        s_status = status.HTTP_201_CREATED
        return s_status
    return serializer.errors


def UpdateEmployee(request,id):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    if id is None:
        id = python_data.get('id')
        if id is None:
            s_status = status.HTTP_400_BAD_REQUEST
            return s_status
    try:
        specific_employee_obj = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return False
    else:
        if request.method == 'PUT':
            serializer = EmployeeSerializer(specific_employee_obj, data=python_data)
        else:
            serializer = EmployeeSerializer(specific_employee_obj, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            s_status = status.HTTP_201_CREATED
            return s_status
        return serializer.errors


def DeleteEmployee(request, id):
    if id is None:
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is None:
            s_status = status.HTTP_400_BAD_REQUEST
            return s_status
    try:
        specific_employee_obj = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return False
    else:
        specific_employee_obj.delete()
        s_status = status.HTTP_200_OK
        return s_status






