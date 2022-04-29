from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.category.models import Category
from apps.category.serializer import CategorySerializer
from api.pagination import CustomPagination, PaginationAPIView


class CategoryView(PaginationAPIView):
    pagination_class = CustomPagination

    """
    Category information view
    """

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = Category.objects.filter(id=pk)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
