"""
in this file we declare all url patterns
through which we have to access data
"""

""" required for admin page """
from django.contrib import admin

"""Returns an element for inclusion in urlpatterns"""
from django.urls import re_path

"""this is our file in which we have written all methods"""
from employees import views

import users.views
"""in this list we have defined all url patterns"""
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^organisation/employees/$', views.EmployeeAPI.as_view()),
    re_path(r'^organisation/employees/(?P<id>\d+)/$', views.EmployeeAPI.as_view()),
    re_path(r'^organisation/employees/search/$', views.EmployeeList.as_view()),

    re_path(r'^organisation/users/$', users.views.UsersAPI.as_view()),
    re_path(r'^organisation/users/(?P<id>\d+)/$', users.views.UsersAPI.as_view()),

]

