"""

class - Users
according to this class our database table will be created

"""

from django.db import models


class Users(models.Model):
    user_no = models.IntegerField()
    user_name = models.CharField(max_length=70)
    user_app = models.CharField(max_length=200)

