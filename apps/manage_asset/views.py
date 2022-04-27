from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from api.pagination import CustomPagination, PaginationAPIView
from .models import Manage
# from api.decorators import login_required
# Create your views here.
# @method_decorator(login_required, name='dispatch')
from .serializer import ListAssetSerializer


class ImportManageView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        queryset = Manage.objects.filter(lend_id__stt=4, status=1)
        serializer = ListAssetSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class ExportManageView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        queryset = Manage.objects.filter(lend_id__stt=6, status=2)
        serializer = ListAssetSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)

# class DeleteImportManageView(APIView):
#     def delete(self, request, pk, form=None):
#         queryset = self.get_object(pk)
#
