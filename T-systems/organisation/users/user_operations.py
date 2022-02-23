from .models import Users
from rest_framework import status
from .serializers import UserSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

def DisplayUser(id):
    if id is not None:
        try:
            specific_User_obj = Users.objects.get(id=id)
        except Users.DoesNotExist:
            s_status = status.HTTP_404_NOT_FOUND
            return s_status
        else:
            serializer = UserSerializer(specific_User_obj)
            return serializer.data

    all_User_obj = Users.objects.all()
    serializer = UserSerializer(all_User_obj, many=True)  # if multiple object then many = true
    return serializer.data


def CreateUser(request):
    json_data = request.body  # getting json data and converting to python
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = UserSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        s_status = status.HTTP_201_CREATED
        return s_status
    return serializer.errors


def UpdateUser(request, id):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    if id is None:
        id = python_data.get("id")
        if id is None:
            s_status = status.HTTP_400_BAD_REQUEST
            return s_status
    try:
        specific_User_obj = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return False
    else:
        if request.method == 'PUT':
            serializer = UserSerializer(specific_User_obj, data=python_data)
        else:
            serializer = UserSerializer(specific_User_obj, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            s_status = status.HTTP_201_CREATED
            return s_status
        return serializer.errors


def DeleteUser(request,id):
    if id is None:
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is None:
            s_status = status.HTTP_400_BAD_REQUEST
            return s_status
    try:
        specific_User_obj = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return False
    else:
        specific_User_obj.delete()
        s_status = status.HTTP_200_OK
        return s_status








