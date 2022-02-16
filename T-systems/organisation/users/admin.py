"""
whatever model we create we need to register them over here
"""


from django.contrib import admin
from users.models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_no', 'user_name', 'user_app']
    """this fields will be displayed in admin panel"""


admin.site.register(Users, UsersAdmin)
