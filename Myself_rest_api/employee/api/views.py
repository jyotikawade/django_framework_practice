########################################
# all import statement
########################################


""" The master class-based base view. All other class-based views inherit from this base class."""
from django.views import View

""" importing model  Employee which we have created """
from .models import Employee

""" importing EmployeeSerializer which we have created"""
from .serializers import EmployeeSerializer

""" Renders the request data into JSON, using utf-8 encoding."""
from rest_framework.renderers import JSONRenderer

"""
to returning response
In contrast to HttpRequest objects, which are created automatically by Django,
HttpResponse objects are your responsibility. 
"""
from django.http import HttpResponse, JsonResponse

"""contains Core tools for working with streams"""
import io

"""Parses JSON request content. request.data will be populated with a dictionary of data."""
from rest_framework.parsers import JSONParser

"""for csrf tokens"""
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

"""
Used for read-only endpoints to represent a collection of model instances
Provides a get method handler.
"""
from rest_framework.generics import ListAPIView

""" learning this part """
from django_filters.rest_framework import DjangoFilterBackend


"""
class = EmployeeList
used for get specific employee according to requirement

methods = none
"""

class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['ename', 'eaddr']


"""
class - EmployeeAPI
use to perform get put post delete operation

methods - get post put delete

get    -  displays employee table details , get(self, request, id=None, *args, **kwargs)
          url pattern to access this method = http://127.0.0.1:8000/employee
          input = if id is specified in url specific employee ditails will be displayed

post   -  insert employee detail intable , post(self, request, *args, **kwargs):
          url pattern to access this method = http://127.0.0.1:8000/employee
          input  = employee record in json format

put    -  used to update , put(self, request, *args, **kwargs):
          url pattern to access this method = http://127.0.0.1:8000/employee
          input = employee record in json format
            
delete -  used to delete record ,delete(self, request, *args, **kwargs):
          url pattern to access this method = http://127.0.0.1:8000/employee   
          input = employee record in json format
          
"""


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeAPI(View):

    def get(self, request, id=None, *args, **kwargs):
        if id is not None:
            SpecificEmployee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(SpecificEmployee)
            """ render() Combines a given template with a given context dictionary"""
            """ and returns an HttpResponse object with that rendered text."""
            """ JSONRenderer Renders the request data into JSON, using utf-8 encoding."""
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        AllEmployee = Employee.objects.all()
        serializer = EmployeeSerializer(AllEmployee, many=True)  # if multiple object then many = true
        """this is used to render serialised data into json which is understandable by front end"""
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            json_data = request.body   #getting json data and converting to python 86 78 88
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = EmployeeSerializer(data=pythondata)
            if serializer.is_valid():
                serializer.save()
                Message_to_screen = {'msg': 'data created'}
                json_data = JSONRenderer().render(Message_to_screen)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            emp = Employee.objects.get(id=id)
            """when you dont want to update all fields at that time partial = true"""
            serializer = EmployeeSerializer(emp, data=pythondata, partial=True)
            if serializer.is_valid():
                serializer.save()
                Message_to_screen = {'msg': 'data updated'}
                json_data = JSONRenderer().render(Message_to_screen)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            SpecificEmployee = Employee.objects.get(id=id)
            SpecificEmployee.delete()
            Message_to_screen = {'msg': 'data deleted'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(Message_to_screen)
            # in order to serialise data other than dict , then do safe = FALSE
            # if safe parameter is set to false then it can be any json serializable object
            # first parameter shpuld be dict instance
