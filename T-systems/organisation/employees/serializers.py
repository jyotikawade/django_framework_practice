from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    class - EmployeeSerializer

    inner class - Meta

    """

    class Meta:
        model = Employee
        fields = ['eno', 'ename', 'esal', 'eaddr']

    def validate_eno(self, value):
        """
        field level validation

        parameter -
        ----------
        self:
        The self parameter is a reference to the current instance of the class

        value :
        value for validation

        """
        if value >= 50000:
            raise serializers.ValidationError('invalid eno')
        return value
