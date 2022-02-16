
from django.db import models

"""

class - Employee
according to this class our database table will be created

"""

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=70)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=200)



