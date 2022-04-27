from rest_framework import serializers
from .models import *


class ListAssetSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    employee_name = serializers.SerializerMethodField()
    department_code = serializers.SerializerMethodField()
    device_code = serializers.SerializerMethodField()
    type_name = serializers.SerializerMethodField()
    stt = serializers.SerializerMethodField()

    class Meta:
        model = Manage
        fields = ('id', 'employee_name', 'department_code', 'device_code', 'type_name', 'quantity', 'import_date', 'reason','stt', 'status')

    def get_id(self, obj):
        return obj.id.id

    def get_employee_name(self, obj):
        return obj.id.name

    def get_department_code(self, obj, format=None):
        return obj.id.department_code.code

    def get_device_code(self, obj):
        return obj.lend.device_code

    def get_type_name(self, obj):
        return obj.product.type.name

    def get_stt(self,obj):
        return obj.lend.stt


class AddManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manage
        fields = ('import_date', 'quantity', 'reason', 'status', 'lend', 'id', 'product')





# class ExportRepositorySerializer(serializers.ModelSerializer):
#     id = serializers.SerializerMethodField()
#     employee_name = serializers.SerializerMethodField()
#     department_code = serializers.SerializerMethodField()
#     device_code = serializers.SerializerMethodField()
#     repository_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Manage
#         fields = ('id', 'employee_name', 'department_code', 'device_code', 'repository_name', 'quantity', 'import_date')
#
#     def get_id(self, obj):
#         return obj.id.id
#
#     def get_employee_name(self, obj):
#         return obj.id.name
#
#     def get_department_code(self, obj, format=None):
#         return obj.id.department_code.code

