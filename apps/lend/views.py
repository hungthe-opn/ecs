from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.pagination import CustomPagination, PaginationAPIView
from .models import *
from .serializer import LendSerializer, LendRemoteSerializer

# list bh


class LendView(APIView):
    def get(self, request, format=None):
        queryset = Lend.objects.all()
        serializer = LendSerializer(queryset, many=True)
        return Response(serializer.data)


class ListLentView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self,request, format=None, *args):
        queryset = Lend.objects.all()
        serializer = LendRemoteSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class SearchLendView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request,pk, format=None, *args, **kwargs):
        queryset = Lend.objects.filter(id=pk)
        serializer = LendRemoteSerializer(queryset, many=True)
        if serializer.is_valid():
            result = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


