from django.contrib import admin
from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^empinfo/(?P<id>\d+)/$', views.Employee_Detail),
    re_path(r'^empinfo/$', views.Employee_Detail_All),
    re_path(r'^empapi/$',views.EmployeeAPI.as_view()),
]
