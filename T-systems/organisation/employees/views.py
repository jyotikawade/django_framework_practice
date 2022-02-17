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


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def DisplayEmployeeDetails(request, id=None):
    """
    Parameters
    ----------
    request :
    an HttpRequest object

    id : int, optional
    employee id to display information

    """

    if id is not None:
        try:
            specific_employee_obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({'msg': 'not exist'})
        else:
            serializer = EmployeeSerializer(specific_employee_obj)
            return Response(serializer.data)

    all_employee_obj = Employee.objects.all()
    serializer = EmployeeSerializer(all_employee_obj, many=True)  # if multiple object then many = true
    return Response(serializer.data)


@api_view(['post'])
def CreateEmployeeDetails(request):
    """
    Parameters
    ----------
    request :
    an HttpRequest object

    """
    if request.method == 'POST':
        json_data = request.body  # getting json data and converting to python
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'})
        return Response(serializer.errors)


@api_view(['put'])
def UpdateEmployeeDetails(request):
    """
        Parameters
        ----------
        request :
        an HttpRequest object

    """
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        try:
            specific_employee_obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({'msg': 'id does not exist'})
        else:
            serializer = EmployeeSerializer(specific_employee_obj, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'data updated'})
            return Response(serializer.errors)


@api_view(['delete'])
def DeleteEmployeeDetails(request):
    """
    Parameters
    ----------
    request :
    an HttpRequest object

    """
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        try:
            specific_employee_obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({'msg': 'id does not exist'})
        else:
            specific_employee_obj.delete()
            return Response({'msg': 'data deleted'})
