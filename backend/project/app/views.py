
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import permissions

# Create your views here.
@api_view(('GET',))
@permission_classes((permissions.AllowAny))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def hello_world(request):
    permission_classes = [permissions.IsAuthenticated]
    return Response({"msg": "Hello from Django!"})
