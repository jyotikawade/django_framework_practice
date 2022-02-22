"""
in this file we declare all url patterns
through which we have to access data
"""

""" required for admin page """
from django.contrib import admin

"""Returns an element for inclusion in urlpatterns"""
from django.urls import re_path

"""this is our file in which we have written all methods"""
import employees.views

import users.views

"""in this list we have defined all url patterns"""

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^employees/$', employees.views.EmployeeDetails),
    re_path(r'^employees/(?P<id>\d+)$', employees.views.EmployeeDetails),

    re_path(r'^employees/filter/$', employees.views.EmployeeList.as_view()),

    re_path(r'^users/$', users.views.UserDetails),
    re_path(r'^users/(?P<id>\d+)$', users.views.UserDetails),

]
