from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers
from supers_types.models import Super_Types

@api_view(['GET', 'POST'])
def supers_list(request):
    
    
    if request.method == 'GET':
        supers_type_param = request.query_params.get('type')
        sort_param = request.query_params.get('type')
        supers = Supers.objects.all()
        if supers_type_param:
            supers = supers.filter(supers_type__type=supers_type_param)
        custom_response_dictionary = {}
        supers = supers.filter(supers_type__type='Heroes')
        supers = supers.filter(supers_type__type='Villains')
        custom_response_dictionary[supers.type] = {
            'Heroes': supers.type,
            'Villains': supers.type
        }
        serializer = SupersSerializer(supers, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)   
    if request.method == 'GET':
        serializer = SupersSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
