from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.views import APIView
from api.pagination import CustomPagination,PaginationAPIView
# Create your views here.


class RepositoryView(PaginationAPIView):
    pagination_class = CustomPagination

    queryset = RepositorySerializer(Repository.objects.all(), many=True)
    result = self.paginate_queryset(serializer.data)
    return self.get_paginated_response(result)

