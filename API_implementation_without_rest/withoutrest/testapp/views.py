from django.http import HttpResponse


#  ---------------------------------------------------------------------------------------

def emp_data_view(request):
    emp_data = {
        'eno': 100,
        'ename': 'sunny',
        'esal': 1000,
        'eaddr': 'mumbai'
    }
    resp = '<h1>Employee number = {} <br> employee_name = {} <br> employee_salary = {} <br> ' \
           'employee_address = {}</h1>'.format(emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eaddr'])

    return HttpResponse(resp)


#  ---------------------------------------------------------------------------------------


import json


def emp_data_jsonview(request):  # we want to send json response
    emp_data = {
        'eno': 100,
        'ename': 'sunny',
        'esal': 1000,
        'eaddr': 'mumbai'
    }
    json_data = json.dumps(emp_data)  # converting python dictionary to json
    return HttpResponse(json_data, content_type='application/json')


#  ---------------------------------------------------------------------------------------

from django.http import JsonResponse


def emp_data_jsonview2(request):  # we want to send json response directly using jsonresponse
    emp_data = {
        'eno': 100,
        'ename': 'sunny',
        'esal': 1000,
        'eaddr': 'mumbai'
    }

    return JsonResponse(emp_data)


#   ---------------------------------------------------------------------------------------
#  class based view

'''
from django.views.generic import View


class JsonCBV(View):  # child class of View
    def get(self, request, *args, **kwargs):        # *args **kwargs is for variable number of argument
        emp_data = {                                # request type will be automatically mapped
            'eno': 100,                             # in View class get method is there we are overriding it
            'ename': 'sunny',
            'esal': 1000,
            'eaddr': 'mumbai'
        }

        return JsonResponse(emp_data)

'''

#   ---------------------------------------------------------------------------------------
# second tryout of class based view

from django.views.generic import View
from testapp.mixins import HttpResponseMixin


class JsonCBV(HttpResponseMixin, View):  # child class of View, HttpResponseMixin
    def get(self, request, *args, **kwargs):  # *args **kwargs is for variable number of argument
        json_data = json.dumps({'msg': 'this is from get method'})
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):  # *args **kwargs is for variable number of argument
        json_data = json.dumps({'msg': 'this is from post method'})
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):  # *args **kwargs is for variable number of argument
        json_data = json.dumps({'msg': 'this is from put method'})
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):  # *args **kwargs is for variable number of argument
        json_data = json.dumps({'msg': 'this is from delete method'})
        return self.render_to_http_response(json_data)