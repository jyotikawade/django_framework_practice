import json
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerialiseMixin
#from django.views.decorators.csrf import csrf_exempt
#from django.utils.decorators import method_decorator
#from testapp.utils import is_json
#from testapp.forms import EmployeeForm


class EmployeeDetailCBV(View):
    # get method for perticular employee
    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'resouse not vailable'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        else:
            json_data = serialize('json', [emp, ], fields=('eno', 'ename', 'eaddr'))

            # output [{"model": "testapp.employee", "pk": 2, "fields": {"eno": 200, "ename": "bunny", "eaddr": "hydrabad"}}]

            return HttpResponse(json_data, content_type='application/json', status=200)


# ---------------------------------------------------------------------------------------------------------------------
#@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailListCBV(SerialiseMixin, View):
    # get method for all employee
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json', status=200)

