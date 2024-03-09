from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def json_test_view(request):
    return JsonResponse({"active": True})