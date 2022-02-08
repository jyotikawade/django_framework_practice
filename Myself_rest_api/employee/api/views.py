from django.views import View
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def Employee_Detail(request, id):
    emp = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(emp)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)  # can do work in one line


# all employee data
def Employee_Detail_All(request):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeAPI(View):
    """
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id', None)
            if id is not None:
                emp = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(emp)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            emp = Employee.objects.all()
            serializer = EmployeeSerializer(emp, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
    """

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = EmployeeSerializer(data=pythondata)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'data created'}
                json_data = JSONRenderer().render(res)
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
            serializer = EmployeeSerializer(emp, data=pythondata, partial=True)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'data created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            emp = Employee.objects.get(id=id)
            emp.delete()
            res = {'msg': 'data created'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)
