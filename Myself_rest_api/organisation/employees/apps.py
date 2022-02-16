from django.apps import AppConfig

"""
whatever apps we create we need to register them over here
"""

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employees'
