from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# from api.employees.models import Employees
from .serializers import DepartmentLendSerializer
from .models import *


# Create your views here.


class EmployeesView(APIView):
    def get(self, request, format=None, *args):
        queryset = DepartmentModel.objects.all()
        serializer = DepartmentLendSerializer(queryset, many=True)
        return Response(serializer.data)
