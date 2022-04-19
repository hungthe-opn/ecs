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



class RepositoryPostType(APIView):
    serializers_class = RepositorySerializer

    def post(self, request, format = None):
        data = self.request.data
        name = data['type_name']
        queryset = Repository.objects.order_by('repository_id').filter(repo__iexact = name)
        serializer = RepositorySerializer(queryset, data)
        return Response(serializer.data)
