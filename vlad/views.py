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
        # print(json.loads(request.body))
        for k, v in json.loads(request.body).items():
            # print(k, v)
            x = Currency(cur=k, value=v)
            x.save()
    return JsonResponse({'status': 'works'})

@csrf_exempt
def show(request):
    if request.method == 'GET':
        # print(list(Currency.objects.all().values('cur', 'value')))
        cur = list(Currency.objects.all().values('cur', 'value'))
        # cur = serializers.serialize('json', Currency.objects.all().values('cur', 'value'))
        # print(cur)
        return JsonResponse(cur, safe=False)