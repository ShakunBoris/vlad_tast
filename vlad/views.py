from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    cur = Currency.objects.all()
    return render(request, 'vlad/index.html', {'cur': cur})

def put
