from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for Tm
from .serializers import TmSerializer
# Tm model
from .models import Tm

# Create your views here.

@csrf_exempt
def tms(request):
    '''
    List all tm records snippets
    '''
    if(request.method == 'GET'):
        # get all the tasks
        tms = Tm.objects.all()
        # serialize the task data
        serializer = TmSerializer(tms, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = TmSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def tm_detail(request, pk):
    try:
        # obtain the task with the passed id.
        tm = Tm.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'GET'):
        serializer = TmSerializer(tm)
        return JsonResponse(serializer.data, status=201)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = TmSerializer(tm, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the task
        tm.delete() 
        # return a no content response.
        return HttpResponse(status=204) 