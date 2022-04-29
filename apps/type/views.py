from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.pagination import CustomPagination, PaginationAPIView
from apps.type.models import *
from apps.type.serializer import TypeSerializer
from api.utils import custom_response
# from api.decorators import login_required


# @method_decorator(login_required, name='dispatch')
class TypeView(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request):
        queryset = Type.objects.all().prefetch_related('repository')
        serializer = TypeSerializer(queryset, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


