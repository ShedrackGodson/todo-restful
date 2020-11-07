from rest_framework.decorators import api_view
# from django.db.models import DoesNotExist
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-details/<int:pk>/",
        "Create": "/task-create/",
        "Update": "/task-update/<int:pk>/",
        "Delete": "/task-delete/<int:pk>/",
    }
    return Response(api_urls)


@api_view(['GET']) # This allows only GET Method
def task_list(request):
    tasks = Task.objects.all()[::-1] # Querying our objects
    serializer = TaskSerializer(tasks, many=True) # Serializing our objects to get Json Objects
    return Response(serializer.data, status=200) # Returning the serialized data


@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk) # Querying our object
    except Task.DoesNotExist:
        return Response("Object Not Available", status=404)
    serializer = TaskSerializer(task, many=False) # Serializing our object to get Json Object
    return Response(serializer.data,status=200)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=200)


@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=200)


@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response("Object Does not exists.", status=404)
    task.delete()
    return Response("Item successfully deleted.", status=200)

