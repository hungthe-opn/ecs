from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.pagination import CustomPagination, PaginationAPIView
from api.utils import convert_date_front_to_back
from .models import *
from .serializer import LendSerializer, LendRemoteSerializer, LendAssetSerializer, DeviceLendSerializer, \
    CreateDeviceSerializer


class LendView(APIView):
    def get(self, request, format=None):
        queryset = Lend.objects.all()
        serializer = LendSerializer(queryset, many=True)
        return Response(serializer.data)


class ListLentView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, format=None, *args):
        queryset = Lend.objects.filter(stt=2)

        # request id params
        if request.query_params.get('employees_id'):
            queryset = queryset.filter(id=request.query_params.get('employees_id'))
        serializer = LendRemoteSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class SearchLendView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, pk, format=None, *args, **kwargs):
        queryset = Lend.objects.filter(id=pk)
        serializer = LendRemoteSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class EndRemoteView(PaginationAPIView):
    pagination_class = CustomPagination

    def post(self, request, pk, format=None, *args, **kwargs):
        lend = Lend.objects.filter(lend_id=pk).first()
        lend.stt = 1
        lend.save()
        return Response({
            'message': 'OK'
        })


class CreateRemoteView(APIView):
    serializer_class = LendRemoteSerializer()

    def post(self, request, *args):
        data = request.data
        print(data)
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadRemoteView(APIView):

    def patch(self, request, pk, format=None):
        queryset = Lend.objects.filter(lend_id=pk).first()
        data = request.data
        # time type conversion
        if data.get('rent_time'):
            data['rent_time'] = convert_date_front_to_back(data.get('rent_time'))
        if data.get('pay_time'):
            data['pay_time'] = convert_date_front_to_back(data.get('pay_time'))

        serializer = LendRemoteSerializer(queryset, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetDepartmentsView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, format=None, *args):
        queryset = Lend.objects.filter(stt=1)
        serializer = LendAssetSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class ListDepartmentsView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, *args,):
        queryset = Lend.objects.filter(stt=1)
        if request.query_params.get('department_code'):
            queryset = queryset.filter(id__department_code__code=request.query_params.get('department_code'))
        serializer = LendAssetSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class DeviceLendView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, format=None):
        queryset = Lend.objects.filter(stt=3)
        serializer = DeviceLendSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class DeviceLendSerializer(APIView):
    def post(self, request, format=None):
        data = request.data
        data['stt'] = 3
        serializer = CreateDeviceSerializer(data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
