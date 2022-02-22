""" importing model  Users which we have created """
from .models import Users

""" importing UserSerializer which we have created"""
from .serializers import UserSerializer

"""contains Core tools for working with streams"""
import io

"""Parses JSON request content. request.data will be populated with a dictionary of data."""
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status


@api_view(['GET', 'post', 'put', 'patch', 'delete'])
def UserDetails(request, id=None):

    if request.method == 'GET':
        if id is not None:
            try:
                specific_User_obj = Users.objects.get(id=id)
            except Users.DoesNotExist:
                return Response({'msg': 'not exist'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = UserSerializer(specific_User_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)

        all_User_obj = Users.objects.all()
        serializer = UserSerializer(all_User_obj, many=True)  # if multiple object then many = true
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        json_data = request.body  # getting json data and converting to python
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = UserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT' or request.method == 'PATCH':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        if id is None:
            id = python_data.get("id")
            if id is None:
                return Response({'msg': 'enter id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            specific_User_obj = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if request.method == 'PUT':
                serializer = UserSerializer(specific_User_obj, data=python_data)
            else:
                serializer = UserSerializer(specific_User_obj, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if id is None:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            if id is None:
                return Response({'msg': 'enter id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            specific_User_obj = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            specific_User_obj.delete()
            return Response({'msg': 'data deleted'}, status=status.HTTP_200_OK)
