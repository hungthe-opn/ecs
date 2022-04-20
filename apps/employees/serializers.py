from rest_framework import serializers
from .models import Employees, AssetEmployeeModel,DepartmentModel
from api.utils import convert_date_back_to_front
from ..category.models import Category


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


class DepartmentLendSerializer(serializers.ModelSerializer):
    lend_device = serializers.SerializerMethodField()

    class Meta:
        model = DepartmentModel
        fields = ('id', 'code', 'lend_device')

    def get_lend_device(self, obj):
        result = dict()
        categories = Category.objects.all()
        total = 0
        for category in categories:
            counter = 0
            emps = obj.department_employees.all()
            for e in emps:
                counter += e.lend.all().filter(product_id__type_id__category_id=category.category_id).count()
            result[category.name] = counter
            total += counter
        result['total'] = total
        return result

