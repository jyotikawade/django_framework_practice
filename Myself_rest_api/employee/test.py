import json

import requests

URL = "http://127.0.0.1:8000/empapi/"

# for get logic two for perticular id
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# for inserting
def post_data():
    data = {'id': '6', 'eno': 5500, 'ename': 'mona', 'esal': 80000, 'eaddr': 'pune', }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


#update data
def update_data():
    data = {'id': 4, 'eno': 5050, 'ename': 'rohit', 'esal': 21000, 'eaddr': 'mumbai', }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# for delete
def delete_data():
    i_id = input("enter id no to delete")
    data = {'id': i_id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


if __name__ == '__main__':
    print("\nget all result:- \n\n")
    get_data()
    print("\n----------------------------------------------------------------------------------------------")

    print("\nget  result for perticular id:- \n\n")
    get_data(1)
    print("\n----------------------------------------------------------------------------------------------")

    print("\npost tryout:- \n\n")
    post_data()
    print("\n----------------------------------------------------------------------------------------------")

    print("\nupdate tryout:- \n\n")
    update_data()
    print("\n----------------------------------------------------------------------------------------------")

    print("\ndelete tryout:- \n\n")
    delete_data()
    print("\n----------------------------------------------------------------------------------------------")

