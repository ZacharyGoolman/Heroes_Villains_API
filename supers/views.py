from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from supers_types.serializers import SuperTypeSerializer
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
            serializer = SupersSerializer(supers, many=True) 
            return Response(serializer.data)

        custom_response_dictionary = {}
        super_hero = supers.filter(supers_type__type='Heroes')
        super_villain = supers.filter(supers_type__type='Villains')
        super_hero_serializer = SupersSerializer(super_hero, many=True)
        super_villain_serializer = SupersSerializer(super_villain, many=True)
        custom_response_dictionary['supers'] = {
            'Heroes': super_hero_serializer.data,
            'Villains': super_villain_serializer.data
        }
        return Response(custom_response_dictionary)

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
