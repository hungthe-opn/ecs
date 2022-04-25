from django.shortcuts import render
from django.utils.decorators import method_decorator
from api.pagination import CustomPagination, PaginationAPIView
from .models import Manage
# from api.decorators import login_required
# Create your views here.
# @method_decorator(login_required, name='dispatch')
from .serializer import ListAssetSerializer


class ListAssetView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        queryset = Manage.objects.all()
        serializer = ListAssetSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)