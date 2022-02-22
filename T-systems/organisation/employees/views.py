"""all import statement"""

""" importing model  Employee which we have created """
from .models import Employee

""" importing EmployeeSerializer which we have created"""
from .serializers import EmployeeSerializer

"""contains Core tools for working with streams"""
import io

"""Parses JSON request content. request.data will be populated with a dictionary of data."""
from rest_framework.parsers import JSONParser

"""
Used for read-only endpoints to represent a collection of model instances
Provides a get method handler.
"""
from rest_framework.generics import ListAPIView

""" learning this part """
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

class EmployeeList(ListAPIView):
    """
    class = EmployeeList
    used for get specific employee according to requirement
    ...
    methods
    ------------
    none
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['ename', 'eaddr']


@api_view(['GET', 'post', 'put', 'patch', 'delete'])
def EmployeeDetails(request, id=None):
    """
    Parameters
    ----------
    request :
    an HttpRequest object

    id : int, optional
    employee id to display information
    """
    if request.method == 'GET':
        if id is not None:
            try:
                specific_employee_obj = Employee.objects.get(id=id)
            except Employee.DoesNotExist:
                return Response({'msg': 'not exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = EmployeeSerializer(specific_employee_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)

        all_employee_obj = Employee.objects.all()
        serializer = EmployeeSerializer(all_employee_obj, many=True)  # if multiple object then many = true
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        json_data = request.body  # getting json data and converting to python
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT' or request.method == 'PATCH':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        if id is None:
            id = python_data.get('id')
            if id is None:
                return Response({'msg': 'enter id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            specific_employee_obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if request.method == 'PUT':
                serializer = EmployeeSerializer(specific_employee_obj, data=python_data)
            else:
                serializer = EmployeeSerializer(specific_employee_obj, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if id is None:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            if id is None:
                return Response({'msg': 'enter id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            specific_employee_obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            specific_employee_obj.delete()
            return Response({'msg': 'data deleted'}, status=status.HTTP_200_OK)

