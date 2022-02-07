import json

from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize


class EmployeeDetailCBV(View):
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)

        '''
                # converting data into dictionary
                emp_data = {
                    'eno': emp.eno,
                    'ename': emp.ename,
                    'esal' : emp.esal,
                    'eaddr' : emp.eaddr
                }
                # convert python dictionary to json object
                json_data = json.dumps(emp_data)
        '''

        # json_data = serialize('json', [emp, ])   #saves above code

        # [emp,] = we want to pass query set
# o/p [{"model": "testapp.employee", "pk": 2, "fields": {"eno": 200, "ename": "bunny", "esal":2000, "eaddr": "hydrabad"}}]

        json_data = serialize('json', [emp, ], fields=('eno', 'ename', 'eaddr'))

# output [{"model": "testapp.employee", "pk": 2, "fields": {"eno": 200, "ename": "bunny", "eaddr": "hydrabad"}}]
        return HttpResponse(json_data, content_type='application/json')
