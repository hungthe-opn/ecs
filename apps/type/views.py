from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.type.models import *
from apps.type.serializer import TypeSerializer
from api.utils import custom_response
# Create your views here.


