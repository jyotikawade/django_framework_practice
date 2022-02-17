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


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def DisplayUserDetails(request, id=None):
    """
    Parameters
    ----------
    request :
    an HttpRequest object

    id : int, optional
    User id to display information

    """

    if id is not None:
        try:
            specific_User_obj = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response({'msg': 'not exist'})
        else:
            serializer = UserSerializer(specific_User_obj)
            return Response(serializer.data)

    all_User_obj = Users.objects.all()
    serializer = UserSerializer(all_User_obj, many=True)  # if multiple object then many = true
    return Response(serializer.data)


@api_view(['post'])
def CreateUserDetails(request):
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
        serializer = UserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'})
        return Response(serializer.errors)


@api_view(['put'])
def UpdateUserDetails(request):
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
            specific_User_obj = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response({'msg': 'id does not exist'})
        else:
            serializer = UserSerializer(specific_User_obj, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'data updated'})
            return Response(serializer.errors)


@api_view(['delete'])
def DeleteUserDetails(request):
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
            specific_User_obj = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response({'msg': 'id does not exist'})
        else:
            specific_User_obj.delete()
            return Response({'msg': 'data deleted'})

