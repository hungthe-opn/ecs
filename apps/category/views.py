from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from apps.category.models import Category
from apps.category.serializer import CategorySerializer
from api.pagination import CustomPagination, PaginationAPIView

 # Create your views here.


class CategoryView(PaginationAPIView):
    pagination_class = CustomPagination
    """
    Category information view
    """

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class CategoryDetailView(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
