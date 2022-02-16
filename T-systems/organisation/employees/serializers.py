
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    """
    class - EmployeeSerializer

    methods
    -------

    create:
    revoked while post request
    update:
    revoked while put request
    """

    class Meta:
        model = Employee
        fields = ['eno', 'ename', 'esal', 'eaddr']

    def create(self, validated_data):
        """
            parameter -
            ----------
            self:
            The self parameter is a reference to the current instance of the class

            validated_data:
            object for validation

        """
        return Employee.objects.create(**validated_data)
                #Employee is table name

    def update(self, instance, validated_data):
        """
        parameter -
        ----------
        self:
        The self parameter is a reference to the current instance of the class

        instance :
        old data stored in database

        validated data:
        new data from user for updation

        """

        instance.eno = validated_data.get('eno', instance.eno)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.eaddr = validated_data.get('eaddr', instance.eaddr)
        instance.save()
        return instance
