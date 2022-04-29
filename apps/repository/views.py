from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.views import APIView
from api.pagination import CustomPagination, PaginationAPIView


class RepositoryView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request):
        queryset = Repository.objects.all()
        serializer = RepositorySerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class RepositoryPostType(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, pk):
        queryset = Repository.objects.filter(type=pk)
        serializer = RepositorySerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)

    def patch(self, request, pk, format=None):
        queryset = Repository.objects.filter(id=pk).first()
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description')
        }
        serializer = RepositorySerializer(queryset, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


class AddProductView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, pk):
        queryset = Repository.objects.filter(id=pk)
        serializer = AddRepositorySerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)

    def post(self, request, pk, format=None):
        data = self.request.data
        quantity = data['quantity']
        print(quantity)
        repository = Repository.objects.filter(id=pk).first()
        repository.quantity += quantity
        repository.save()
        serializer = AddRepositorySerializer(repository)
        return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)


class RepositoryListView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request):
        queryset = Repository.objects.all()
        serializer = QuantitySerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)