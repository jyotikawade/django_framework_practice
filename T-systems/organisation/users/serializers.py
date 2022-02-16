
from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):

    """
    class - EUserSerializer

    methods
    -------

    create:
    revoked while post request
    update:
    revoked while put request

    """

    class Meta:
        model = Users
        fields = ['user_no', 'user_name', 'user_app']

    def create(self, validated_data):
        """
            parameter -
            ----------
            self:
            The self parameter is a reference to the current instance of the class

            validated_data:
            object for validation

        """
        return Users.objects.create(**validated_data)
                #Users is table name

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

        instance.user_no = validated_data.get('user_no', instance.user_no)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_app = validated_data.get('user_app', instance.user_app)
        instance.save()
        return instance
