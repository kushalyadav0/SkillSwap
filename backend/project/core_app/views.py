from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions

# Create your views here.

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def hello(request):
    permission_classes = ([permissions.BasePermissionMetaclass])
    return Response({'msg':'Hello!'})