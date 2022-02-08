import json

import requests

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


def get_resourse():
    id = input("enter id")
    resp = requests.get(BASE_URL + END_POINT + id + '/')
    print(resp.status_code)
    print(resp.json())


def get_all():
    resp = requests.get(BASE_URL + END_POINT)
    print(resp.status_code)
    print(resp.json())


def create_resourse():
    new_emp = {'eno': 600, 'ename': 'sona', 'esal': 80333, 'eaddr': 'pune', }

    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


if __name__ == '__main__':
     get_resourse()
     print("\n\n------------------------------displaying all employee------------------------------------")
     get_all()
    #create_resourse()
