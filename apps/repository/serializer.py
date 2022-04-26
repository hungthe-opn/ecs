from rest_framework import serializers
from apps.repository.models import Repository


class RepositorySerializer(serializers.ModelSerializer):
    type_id = serializers.SerializerMethodField()
    type_name = serializers.SerializerMethodField()

    class Meta:
        model = Repository
        fields = ('type_id', 'type_name', 'name', 'quantity', 'color', 'description')

    def get_type_id(self, obj, format=None):
        return obj.type_id

    def get_type_name(self, obj, format=None):
        return obj.type.name


class AddRepositorySerializer(serializers.ModelSerializer):
    type_id = serializers.SerializerMethodField()
    type_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Repository
        fields = ('category_name', 'type_name', 'name', 'quantity', 'type_id', 'product_id')

    def get_type_id(self, obj, format=None):
        return obj.type_id

    def get_type_name(self, obj, format=None):
        return obj.type.name

    def get_category_name(self, obj, format=None):
        return obj.type.category.name


class AddsRepositorySerializer(serializers.ModelSerializer):
    type_id = serializers.SerializerMethodField()
    type_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Repository
        fields = ('category_name', 'type_id', 'type_name', 'name', 'quantity', 'color', 'description')

    def get_type_id(self, obj, format=None):
        return obj.type_id

    def get_type_name(self, obj, format=None):
        return obj.type.name

    def get_category_name(self, obj, format=None):
        return obj.type.category.name