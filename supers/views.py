from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers


@api_view(['GET', 'POST'])
def supers_list(request):
    supers = get_object_or_404(Supers)
    request.method == 'GET'
    serializer = SupersSerializer
    return response(serializer.data)
def supers_detail
        