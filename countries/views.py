#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NATIVE DJANGO
from django.http.request import HttpRequest
from django.shortcuts import render
from django.http.response import JsonResponse

# REST FRAMEWORK
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

# Countries APP
from countries.models import Countries
from countries.serializers import CountriesSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def countries_list(request: HttpRequest):
    """
    API View to list all countries or to add new ones

    :param request: GET or POST Requests
    :type request: HttpRequest
    :return: JSON RESPONE
    :rtype: json
    """
    if request.method == 'GET':
        countries = Countries.objects.all() # pylint: disable=maybe-no-member

        name = request.GET.get('name', None)
        if name is not None:
            countries = countries.filter(name__icontains=name)
        
        countries_serializer = CountriesSerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)
    
    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(data=countries_data)

        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def countries_detail(request:HttpRequest, pk):
    """
    API View to get or update or delete a country by a given primary key

    :param request: GET, PUT or DELETE Request
    :type request: HttpRequest
    :param pk: Country Primary Key
    :type pk: int
    :return: JSON RESPONSE
    :rtype: json
    """
    try:
        countries:Countries = Countries.objects.get(pk=pk) # pylint: disable=maybe-no-member
    except:
        return JsonResponse({'message': 'The country does not exists'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        countries_serializer = CountriesSerializer(countries)
        return JsonResponse(countries_serializer.data)
    
    elif request.method == 'PUT':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(countries, data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data)
        
        return JsonResponse(countries_serializer.errors, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        countries.delete()
        return JsonResponse({'message': 'Country was deleted succesfully!'}, status = status.HTTP_204_NO_CONTENT)
