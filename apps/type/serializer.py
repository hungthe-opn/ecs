from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    category_id = serializers.SerializerMethodField()

    class Meta:
        model = Type
        fields = ('type', 'name', 'category_id', 'quantity')