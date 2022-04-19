from rest_framework import serializers
from .models import *
from apps.category.serializer import CategorySerializer


class TypeSerializer(serializers.ModelSerializer):
    category_id = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    counters = serializers.SerializerMethodField()
    class Meta:
        model = Type
        fields = ('type_id', 'name', 'category', 'counters', 'category_id', 'category_name',)

    def get_category_id(self, obj):
        return obj.category_id

    def get_category_name(self, obj):
        return obj.category.name

    def get_counters(self,obj):
        repository = obj.repository.all()

        counters = 0
        for r in repository:
            counters+=r.quantity
        return counters