"""all import statement"""
import json

""" The master class-based base view. All other class-based views inherit from this base class."""
from django.views import View

""" importing model  Users which we have created """
from .models import Users

""" importing UserSerializer which we have created"""
from .serializers import UserSerializer

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


@method_decorator(csrf_exempt, name='dispatch')
class UsersAPI(View):
    """
    class - UsersAPI
    use to perform get put post delete operation
    ...

    methods
    ------------

    get    -  displays Users table details , get(self, request, id=None, *args, **kwargs)
              input = if id is specified in url specific Users ditails will be displayed

    post   -  insert Users detail intable , post(self, request, *args, **kwargs):
              input  = Users record in json format

    put    -  used to update , put(self, request, *args, **kwargs):
              input = Users record in json format

    delete -  used to delete record ,delete(self, request, *args, **kwargs):
              input = Users record in json format

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
        Users id to display information

        *args
        variable number of arguments to a function.
        It is used to pass a non-key worded, variable-length argument list.

        **kwargs
        used to pass a keyworded argument,
        variable-length argument list.

        """

        if id is not None:
            try:
                specific_Users_obj = Users.objects.get(id=id)
            except Users.DoesNotExist:
                json_data = json.dumps({'msg': 'not exist'})
                return HttpResponse(json_data, content_type='application/json')
            else:
                serializer = UserSerializer(specific_Users_obj)
                """ render() Combines a given template with a given context dictionary"""
                """ and returns an HttpResponse object with that rendered text."""
                """ JSONRenderer Renders the request data into JSON, using utf-8 encoding."""
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')

        all_Users_obj = Users.objects.all()
        serializer = UserSerializer(all_Users_obj, many=True)  # if multiple object then many = true
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
            json_data = request.body  # getting json data and converting to python
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = UserSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                Message_to_screen = {'msg': 'data created'}
                json_data = JSONRenderer().render(Message_to_screen)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
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
        if request.method == 'PUT':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            try:
                specific_Users_obj = Users.objects.get(id=id)
            except Users.DoesNotExist:
                json_data = json.dumps({'msg': 'id does not exist'})
                return HttpResponse(json_data, content_type='application/json')
            else:
                """when you dont want to update all fields at that time partial = true"""
                serializer = UserSerializer(specific_Users_obj, data=python_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    Message_to_screen = {'msg': 'data updated'}
                    json_data = JSONRenderer().render(Message_to_screen)
                    return HttpResponse(json_data, content_type='application/json')
                json_data = JSONRenderer().render(serializer.errors)
                return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
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
        if request.method == 'DELETE':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            try:
                specific_Users_obj = Users.objects.get(id=id)
            except Users.DoesNotExist:
                json_data = json.dumps({'msg': 'id does not exist'})
                return HttpResponse(json_data, content_type='application/json')
            else:
                specific_Users_obj.delete()
                Message_to_screen = {'msg': 'data deleted'}
                # json_data = JSONRenderer().render(res)
                # return HttpResponse(json_data, content_type='application/json')
                return JsonResponse(Message_to_screen)
                # in order to serialise data other than dict , then do safe = FALSE
                # if safe parameter is set to false then it can be any json serializable object
                # first parameter shpuld be dict instance
