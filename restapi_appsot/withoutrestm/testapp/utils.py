# we are creating this file to check corresponding application is sending json data or not


import json


def is_json(data):
    try:
        p_data = json.loads(data)   # if data is not json data then this loads function going  to fail
        valid = True
    except ValueError:
        valid = False
    return valid

