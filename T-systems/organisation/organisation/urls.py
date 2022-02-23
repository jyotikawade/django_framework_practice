"""
in this file we declare all url patterns
through which we have to access data
"""

from django.contrib import admin
from django.urls import re_path
import employees.views
import users.views

"""in this list we have defined all url patterns"""
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^employees', employees.views.EmployeeDetails),
    re_path(r'^employees/filter/$', employees.views.EmployeeList.as_view()),
    re_path(r'^users', users.views.UserDetails),



]
