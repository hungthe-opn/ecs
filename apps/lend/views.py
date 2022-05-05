from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.pagination import CustomPagination, PaginationAPIView
from api.utils import convert_date_front_to_back, custom_response
from .models import *
from .serializer import LendSerializer, DeviceLendSerializer, \
     InsuranceSerializer, NotifySerializer, AddRemotesSerializer, \
    ListLendRemoteSerializer, ListLendAssetSerializer, AddDeviceSerializer, AssetExportSerializer
from datetime import date, timedelta
from django.db.models import Q
from ..manage_asset.serializer import AddManagerSerializer


class LendView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request):
        queryset = Lend.objects.all()
        serializer = LendSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class ListLentView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, format=None, *args):
        """
        Pass employee_id from params return list stt=2
        """
        queryset = Lend.objects.filter(stt=2)
        if request.query_params.get('employees_id'):
            queryset = queryset.filter(employee=request.query_params.get('employees_id'))
        serializer = ListLendRemoteSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class SearchLendView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, pk, format=None, *args, **kwargs):

        """
         Return list employee_id = pk
        """

        queryset = Lend.objects.filter(employee=pk, stt=2)
        serializer = ListLendRemoteSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class EndRemoteView(APIView):
    def post(self, request, pk, format=None, *args, **kwargs):
        """

        """
        lend = Lend.objects.filter(id=pk).first()
        lend.stt = 1
        print(lend.__dict__)
        lend.save()
        return Response({
            'message': 'Successful conversion !'
        })


class UploadRemoteView(APIView):
    def patch(self, request, pk, format=None):
        """

        """
        queryset = Lend.objects.filter(id=pk).first()
        data = request.data
        if data.get('rent_time'):
            data['rent_time'] = convert_date_front_to_back(data.get('rent_time'))
        if data.get('pay_time'):
            data['pay_time'] = convert_date_front_to_back(data.get('pay_time'))

        serializer = ListLendRemoteSerializer(queryset, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(custom_response(serializer.data, msg_display='Chỉnh sửa lại thời gian bảo hành thành công.'),
                            status=status.HTTP_201_CREATED)
        return Response(custom_response(serializer.errors, response_code=400, response_msg='ERROR',
                                        msg_display='Chỉnh sửa lại thời gian remote thuất bại. Vui lòng kiểm tra lại'),
                        status=status.HTTP_400_BAD_REQUEST)


class AssetDepartmentsView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, format=None, *args):
        queryset = Lend.objects.filter(stt=1)
        serializer = ListLendAssetSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class AssetDepartmentsExportView(APIView):

    def get(self, request, pk, format=None):
        queryset = Lend.objects.filter(id=pk)
        serializer = AssetExportSerializer(queryset, many=True)
        return Response(custom_response(serializer.data), status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        data = self.request.data
        data['stt'] = 4

        queryset = Lend.objects.filter(id=pk)
        serializer = AssetExportSerializer(queryset, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(custom_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(custom_response(serializer.errors, response_code=400, response_msg='ERROR',
                                        msg_display='Mượn thuất bại. Vui lòng kiểm tra lại'),
                        status=status.HTTP_400_BAD_REQUEST)


class ListDepartmentsView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, *args):
        queryset = Lend.objects.filter(stt=1)
        if request.query_params.get('department_code'):
            queryset = queryset.filter(employee__department_code__code=request.query_params.get('department_code'))
        serializer = ListLendAssetSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class DeviceLendView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request):
        queryset = Lend.objects.filter(stt=3)
        serializer = DeviceLendSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class DeviceLendExportView(APIView):

    def post(self, request):
        data = request.data
        data['stt'] = 3
        serializer = AddDeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(custom_response(serializer.data, msg_display='Xuất mượn thành công.'),
                            status=status.HTTP_201_CREATED)
        return Response(custom_response(serializer.errors, response_code=400, response_msg='ERROR',
                                        msg_display='Xuất mượn thuất bại. Vui lòng kiểm tra lại'),
                        status=status.HTTP_400_BAD_REQUEST)


class InsuranceView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, *args):
        queryset = Lend.objects.filter(stt=6)
        serializer = InsuranceSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class EndInventoryView(APIView):

    def post(self, request, pk):
        insurance = Lend.objects.filter(id=pk, stt=6).first()
        insurance.stt = 1
        insurance.save()
        serializer = InsuranceSerializer(insurance)
        return Response(custom_response(serializer.data, msg_display='Kết thúc thành công'),
                        status=status.HTTP_201_CREATED)


class AddInsuranceView(APIView):
    def patch(self, request, pk, *args, format=None):
        queryset = Lend.objects.filter(id=pk, stt=1).first()
        data = request.data
        queryset.stt = 6
        if data.get('insurance_start'):
            data['insurance_start'] = convert_date_front_to_back(data.get('insurance_start'))
        if data.get('insurance_end'):
            data['insurance_end'] = convert_date_front_to_back(data.get('insurance_end'))

        serializer = InsuranceSerializer(queryset, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(custom_response(serializer.data, msg_display='Thêm thời gian thành công'),
                            status=status.HTTP_201_CREATED)
        return Response(custom_response(serializer.errors, response_code=400, response_msg='ERROR',
                                        msg_display='Thêm thời gian bảo hành thuất bại. Vui lòng kiểm tra lại'),
                        status=status.HTTP_400_BAD_REQUEST)


class NotifyView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, *args):
        today = date.today()
        coming_due_date = today + timedelta(days=10)
        coming_due = Lend.objects.filter(stt=1).filter(Q(pay_time__lte=coming_due_date) |
                                                       Q(pay_time__lte=today))
        serializer = NotifySerializer(coming_due, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class ImportLendRepository(APIView):

    def post(self, request, pk):
        lend = Lend.objects.filter(id=pk).first()
        lend.stt = 4
        lend.save()
        manage = {
            'import_date': date.today(),
            'quantity': 1,
            'reason': request.data.get('reason'),
            'status': 1,
            'lend': lend.id,
            'employee': lend.employee.id,
            'repository': lend.repository.id
        }
        lend.repository.quantity += 1
        lend.repository.save()
        serializer = AddManagerSerializer(data=manage)
        if serializer.is_valid():
            serializer.save()
            return Response(custom_response(serializer.data, msg_display='Nhập thiết bị mượn thành công'),
                            status=status.HTTP_201_CREATED)
        return Response(custom_response(serializer.errors, response_code=400, response_msg='ERROR',
                                        msg_display='Quá trình nhập thuất bại. Vui lòng kiểm tra lại'),
                        status=status.HTTP_400_BAD_REQUEST)


class ExportLendRepository(APIView):

    def post(self, request, pk):
        lend = Lend.objects.filter(id=pk).first()
        lend.stt = 6
        lend.save()
        data = {
            'import_date': date.today(),
            'quantity': 1,
            'reason': request.data.get('reason'),
            'status': 1,
            'lend': lend.id,
            'employee': lend.employee.id,
            'repository': lend.repository.id
        }
        lend.repository.quantity -= 1
        lend.repository.save()
        serializer = AddManagerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(custom_response(serializer.data, msg_display='Nhập thiết bị thành công'),
                            status=status.HTTP_201_CREATED)
        return Response(custom_response(serializer.errors, response_code=400, response_msg='ERROR',
                                        msg_display='Nhập thiết bị thất bại, vui lòng kiểm tra lại'),
                        status=status.HTTP_400_BAD_REQUEST)


class AddRemotedView(APIView):

    def post(self, request):
        data = {
            'employee': request.data.get('employee_id'),
            'repository': request.data.get('repository_id'),
            'quantity': 1,
            'device_code': request.data.get('device_code'),
            'stt': request.data.get('stt')
        }

        if request.data.get('rent_time'):
            data['rent_time'] = convert_date_front_to_back(request.data.get('rent_time'))
        if request.data.get('pay_time'):
            data['pay_time'] = convert_date_front_to_back(request.data.get('pay_time'))
        serializer = AddRemotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            repository = Repository.objects.filter(id=data.get('repository')).first()
            repository.quantity -= 1
            repository.save()
            return Response(custom_response(serializer.data, msg_display='Thêm thiết bị mượn thành công'),
                            status=status.HTTP_201_CREATED)
        return Response(custom_response(serializer.errors, response_code=400, response_msg='ERROR',
                                        msg_display='Thêm thiết bị mượn đã thất bại, vui lòng kiểm tra lại'),
                        status=status.HTTP_400_BAD_REQUEST)
