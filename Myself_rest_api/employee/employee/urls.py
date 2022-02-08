from django.contrib import admin
from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^empapi/$', views.EmployeeAPI.as_view()),

]
