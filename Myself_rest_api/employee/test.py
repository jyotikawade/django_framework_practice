import json

import requests

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'empinfo/'


# for getting perticular resourse
def get_resourse():
    id = input("\n enter id = \n")
    resp = requests.get(BASE_URL + END_POINT + id + '/')
    print(resp.status_code)
    print(resp.json())


# for displaying all obj
def get_all():
    resp = requests.get(BASE_URL + END_POINT)
    print(resp.status_code)
    print(resp.json())


'''
# for get logic two for perticular id
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    URL = "http://127.0.0.1:8000/empapi/"
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
'''

# for inserting
def post_data():
    data = {'eno': 5500, 'ename': 'mona', 'esal': 80000, 'eaddr': 'pune', }
    json_data = json.dumps(data)
    URL = "http://127.0.0.1:8000/empapi/"
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


#update data
def update_data():
    data = {'id': 4, 'eno': 5050, 'ename': 'rohit', 'esal': 21000, 'eaddr': 'mumbai', }
    json_data = json.dumps(data)
    URL = "http://127.0.0.1:8000/empapi/"
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# for delete
def delete_data():
    i_id = input("enter id no to delete")
    data = {'id': i_id}
    json_data = json.dumps(data)
    URL = "http://127.0.0.1:8000/empapi/"
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


if __name__ == '__main__':
    print("\nget all result:- \n\n")
    get_all()
    print("\n----------------------------------------------------------------------------------------------")

    print("\nget  result for perticular id:- \n\n")
    get_resourse()
    print("\n----------------------------------------------------------------------------------------------")

    print("\npost tryout:- \n\n")
    post_data()
    print("\n----------------------------------------------------------------------------------------------")

    print("\npost tryout:- \n\n")
    update_data()
    print("\n----------------------------------------------------------------------------------------------")

    print("\npost tryout:- \n\n")
    delete_data()
    print("\n----------------------------------------------------------------------------------------------")

