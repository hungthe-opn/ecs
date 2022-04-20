from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.views import APIView
from api.pagination import CustomPagination,PaginationAPIView
# Create your views here.


class RepositoryView(APIView):
    serializers_class = RepositorySerializer

    def get(self, request, format=None):
        queryset = Repository.objects.all()
        serializer = RepositorySerializer(queryset,many=True)
        return Response('result', serializer.data)


class RepositoryPostType(APIView):
    serializers_class = RepositorySerializer

    def get(self, request, pk, format=None):
        queryset = Repository.objects.filter(type_id=pk)
        serializer = RepositorySerializer(queryset, many=True)
        return Response({'result': serializer.data})

    def post(self, request, format=None):
        data = self.request.data
        name = data['name']
        print(name)
        queryset = Repository.objects.order_by('product_id').filter(product_id__iexact=name)
        serializer = RepositorySerializer(queryset)
        if serializer.is_valid():
            return Response({'result': serializer.data})
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, pk, format=None, *args,):
        queryset = Repository.objects.filter(product_id=pk).first()
        data = {
            'description': request.data.get('description')
        }
        serializer = RepositorySerializer(queryset, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': serializer.data})
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)