
from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):

    """
    class - UserSerializer
    inner class - Meta

    """

    class Meta:
        model = Users
        fields = ['user_no', 'user_name', 'user_app']


    def validate_user_no(self,value):
        """
        field level validation for user_no

        parameter -
        ----------
        self:
        The self parameter is a reference to the current instance of the class

        value :
        value for validation

        """
        if value>=5000:
            raise serializers.ValidationError('to many users')
        return value