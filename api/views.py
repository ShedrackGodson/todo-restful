from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-details/<str:pk>/",
        "Create": "/task-create/",
        "Update": "/task-update/<str:pk>/",
        "Delete": "/task-delete/<str:pk>/",
    }
    return Response(api_urls)