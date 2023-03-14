from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

# Create your views here.
def index(request):
    # cur = Currency.objects.all()
    # {'cur': cur}
    return render(request, 'vlad/index.html', {})

@csrf_exempt
def save(request):
    if request.method == "POST":
        Currency.objects.all().delete()
        for k, v in json.loads(request.body).items():
            x = Currency(cur=k, value=v)
            x.save()
    return JsonResponse({'status': 'works'})

@csrf_exempt
def show(request):
    if request.method == 'GET':
        cur = list(Currency.objects.all().values('cur', 'value'))
        return JsonResponse(cur, safe=False)