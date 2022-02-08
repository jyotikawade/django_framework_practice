
from django.core.serializers import serialize
import json


class SerialiseMixin(object):
    # to remove extra information we have written this code
    def serialize(self, qs):
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_list = []

        for obj in p_data :
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return json_data

