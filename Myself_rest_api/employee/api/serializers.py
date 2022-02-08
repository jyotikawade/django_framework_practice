from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=70)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.eno = validated_data.get('eno', instance.eno)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.eaddr = validated_data.get('eaddr', instance.eaddr)
        instance.save()
        return instance
