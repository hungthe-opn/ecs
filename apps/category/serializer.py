from rest_framework import serializers
from .models import Category
from api.utils import convert_date_back_to_front


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'name',)

