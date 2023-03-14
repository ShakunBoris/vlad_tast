from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

# Create your views here.
def index(request):
    tb = []
    for i in Parse.objects.all():
        # tb.append(t2.filter(call_id=i))
        if len(i.currency_by_parse.all()) != 0:
            tb.append(i.currency_by_parse.all())
    print(tb)
    return render(request, 'vlad/index.html', {'tb': tb[::-1]})

@csrf_exempt
def save(request):
    if request.method == "POST":
        # Currency.objects.all().delete()
        parse = Parse()
        parse.save()
        for k, v in json.loads(request.body).items():
            x = Currency(cur=k, value=v, call_id=parse)
            x.save()
    return JsonResponse({'status': 'works'})

@csrf_exempt
def show(request):
    if request.method == 'GET':
        cur = list(Parse.objects.last().currency_by_parse.all().values('cur', 'value', 'call_id'))
        # cur = list(Currency.objects.all().values('cur', 'value', 'call_id'))
        return JsonResponse(cur, safe=False)