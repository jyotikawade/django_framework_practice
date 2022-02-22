from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .functionality import CreateEmployee, DisplayEmployee, UpdateEmployee, DeleteEmployee


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
        ret_value = DisplayEmployee(id)
        if ret_value == status.HTTP_404_NOT_FOUND:
            return Response({'msg': 'not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(ret_value, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        ret_value = CreateEmployee(request)
        if ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT' or request.method == 'PATCH':
        ret_value = UpdateEmployee(request, id)
        if ret_value == status.HTTP_400_BAD_REQUEST:
            return Response({'msg': 'enter id'}, status=status.HTTP_400_BAD_REQUEST)
        elif not ret_value:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        elif ret_value == status.HTTP_201_CREATED:
            return Response({'msg': 'data updated'}, status=status.HTTP_201_CREATED)
        return Response(ret_value, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
       ret_value = DeleteEmployee(request, id)
       if ret_value == status.HTTP_400_BAD_REQUEST:
           return Response({'msg': 'enter id in url or in body'}, status=status.HTTP_400_BAD_REQUEST)
       elif not ret_value:
           return Response({'msg': 'id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
       return Response({'msg': 'data deleted'}, status=status.HTTP_200_OK)

