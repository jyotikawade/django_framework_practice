
#sending http reuest to django aplication function based view

'''
import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijson'

resp = requests.get(BASE_URL+ENDPOINT)  # you will get json data as response according to our function specified in views

data = resp.json()  # this function will convert Json response to python dict

print(data)

# python app                                 django app
#  --------------> sending http request-------->
#  <----------- getting json response <-----------


print('\ndata from django application \n')

print('employee number', data['eno'])
print('employee name', data['ename'])
print('employee salary', data['esal'])
print('employee address', data['eaddr'])

'''

# sending request to django application class based view


import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsoncbv'                 # ----- change is only here from previous version
resp = requests.get(BASE_URL+ENDPOINT) # you will get json data as response according to our function specified in views
data = resp.json()  # this function will convert Json response to python dict
print(data)

