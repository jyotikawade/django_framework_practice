"""all import statement"""

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





@method_decorator(csrf_exempt, name='dispatch')
class EmployeeAPI(View):
    """
    class - EmployeeAPI
    use to perform get put post delete operation
    ...

    methods
    ------------

    get    -  displays employee table details , get(self, request, id=None, *args, **kwargs)
              input = if id is specified in url specific employee ditails will be displayed

    post   -  insert employee detail intable , post(self, request, *args, **kwargs):
              input  = employee record in json format

    put    -  used to update , put(self, request, *args, **kwargs):
              input = employee record in json format

    delete -  used to delete record ,delete(self, request, *args, **kwargs):
              input = employee record in json format

    """

    def get(self, request, id=None, *args, **kwargs):
        """
        Parameters
        ----------
        self:
        The self parameter is a reference to the current instance of the class

        request :
        an HttpRequest object

        id : int, optional
        employee id to display information

        *args
        variable number of arguments to a function.
        It is used to pass a non-key worded, variable-length argument list.

        **kwargs
        used to pass a keyworded argument,
        variable-length argument list.

        """
        if id is not None:
            specific_employee_obj = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(specific_employee_obj)
            """ render() Combines a given template with a given context dictionary"""
            """ and returns an HttpResponse object with that rendered text."""
            """ JSONRenderer Renders the request data into JSON, using utf-8 encoding."""
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        all_employee_obj = Employee.objects.all()
        serializer = EmployeeSerializer(all_employee_obj, many=True)  # if multiple object then many = true
        """this is used to render serialised data into json which is understandable by front end"""
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        """
        Parameters
        ----------
        self:
        The self parameter is a reference to the current instance of the class

        request :
        an HttpRequest object

        *args
        variable number of arguments to a function.
        It is used to pass a non-key worded, variable-length argument list.

        **kwargs
        used to pass a keyworded argument,
        variable-length argument list.

        """
        if request.method == 'POST':
            json_data = request.body  # getting json data and converting to python 86 78 88
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = EmployeeSerializer(data=python_data)
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
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            specific_employee_obj = Employee.objects.get(id=id)
            """when you dont want to update all fields at that time partial = true"""
            serializer = EmployeeSerializer(specific_employee_obj, data=python_data, partial=True)
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
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            specific_employee_obj = Employee.objects.get(id=id)
            specific_employee_obj.delete()
            Message_to_screen = {'msg': 'data deleted'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(Message_to_screen)
            # in order to serialise data other than dict , then do safe = FALSE
            # if safe parameter is set to false then it can be any json serializable object
            # first parameter shpuld be dict instance
