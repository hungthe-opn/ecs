from rest_framework import serializers
from .models import Employees, AssetEmployeeModel
from api.utils import convert_date_back_to_front


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    birthday = serializers.SerializerMethodField()

    class Meta:
        model = Employees
        fields = ('id', 'name', 'email', 'address', 'current_address', 'birthday', 'gender', 'phone',
                  'nationality')

    def get_email(self, obj):
        return obj.account.email

    def get_birthday(self, obj):
        if obj.birthday is not None:
            return convert_date_back_to_front(str(obj.birthday))
        return ''


class AssetEmployeeSerializer(serializers.Serializer):
    employee_id = serializers.CharField(max_length=4)

    def create(self, validated_data):
        return AssetEmployeeModel.objects.get_or_create(**validated_data, is_active=True)