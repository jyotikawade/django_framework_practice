"""all import statement"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .user_operations import DisplayUser, CreateUser, UpdateUser, DeleteUser


@api_view(['GET', 'post', 'put', 'patch', 'delete'])
def UserDetails(request, id=None):

    """
        Parameters
        ----------
        request :
        an HttpRequest object

        id : int, optional
        it is employee id to for performing operation
    """

    if request.method == 'GET':
        ret_value = DisplayUser(id)
        if ret_value == status.HTTP_404_NOT_FOUND:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(ret_value, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        ret_value = CreateUser(request)
        if ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'User record created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT' or request.method == 'PATCH':
        ret_value = UpdateUser(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id in url or in body'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        elif ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
        return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        ret_value = DeleteUser(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id in url or in body'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'data deleted'}, status=status.HTTP_200_OK)

