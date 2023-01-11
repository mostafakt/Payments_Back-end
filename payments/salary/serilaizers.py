import logging
from rest_framework import serializers
from .models import paid, Salary
from django.contrib.auth import get_user_model


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class PaidSerilizer(serializers.ModelSerializer):

    class Meta:
        model = paid
        fields = '__all__'

    @classmethod
    def short(cls, *args, **kwargs):
        kwargs.setdefault(fields=('id', 'username', 'salary'))
        return cls(*args, **kwargs)

    @classmethod
    def extended(cls):
        return cls(fields=('id', ))

    @classmethod
    def default(cls):
        class CustomSerializer(cls):
            salary = SalarySerilizer(write_only=True)
        return CustomSerializer()


class SalarySerilizer(serializers.ModelSerializer):
    paids = PaidSerilizer(many=True)

    class Meta:
        model = Salary
        fields = '__all__'
