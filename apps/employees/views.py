from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# from api.employees.models import Employees
from api.pagination import PaginationAPIView, CustomPagination
from .serializers import DepartmentLendSerializer
from .models import *


# Create your views here.


class EmployeesView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, format=None, *args):
        queryset = DepartmentModel.objects.all()
        serializer = DepartmentLendSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)