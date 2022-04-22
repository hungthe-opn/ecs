from rest_framework.response import Response
from rest_framework.views import APIView
from api.pagination import CustomPagination
from apps.type.models import *
from apps.type.serializer import TypeSerializer
from api.utils import custom_response
# from api.decorators import login_required
# Create your views here.


# @method_decorator(login_required, name='dispatch')
class TypeView(APIView):
    pagination_class = CustomPagination

    def get(self, request, format=None):
        queryset = Type.objects.prefetch_related('repository').all()
        serializer = TypeSerializer(queryset, many=True)
        return Response(serializer.data)


