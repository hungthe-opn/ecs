
from .models import *
from api.pagination import CustomPagination, PaginationAPIView
from rest_framework import serializers

from .. import repository


class LendSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    employee_name = serializers.SerializerMethodField()
    department_code = serializers.SerializerMethodField()
    class Meta:
        model = Lend
        fields = ('id', 'department_code', 'employee_name', 'device_code', 'condition', 'rent_time', 'pay_time', 'warranty', 'describe',)

    def get_id(self, obj, format=None):
        return obj.id.id

    def get_employee_name(self, obj, format=None):
        return obj.id.name

    def get_department_code(self, obj, format=None):
        return obj.id.department_code.code


class LendRemoteSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    employee_name = serializers.SerializerMethodField()
    department_code = serializers.SerializerMethodField()
    repository_name = serializers.SerializerMethodField()

    class Meta:
        model = Lend
        fields = ('id', 'employee_name', 'department_code', 'device_code', 'repository_name', 'condition', 'rent_time', 'pay_time', 'created_at', 'updated_at', 'status')

    def get_id(self, obj, format=None):
        return obj.id.id

    def get_employee_name(self, obj, format=None):
        return obj.id.name

    def get_department_code(self, obj, format=None):
        return obj.id.department_code.code

    def get_repository_name(self, obj, format=None):
        return obj.product.name


class DepartmentLendSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    department_code = serializers.SerializerMethodField()

